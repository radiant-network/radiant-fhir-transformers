#!/usr/bin/env python3
"""
CLI tool to run a transformer on a test resource and display the results.

This script dynamically imports a transformer module, loads the corresponding
test resource, runs the transformation, and displays the results in a table.
"""

import argparse
import importlib.util
import os
import sys
from typing import Any

try:
    from tabulate import tabulate
except ImportError:
    print("Error: tabulate library is required. Install it with: pip install tabulate")
    sys.exit(1)


def dynamic_import(filepath: str):
    """
    Import a Python module given a filepath.
    
    Handles relative imports by setting up the module's __package__ attribute
    based on the directory structure.
    
    Args:
        filepath: Path to the Python module file
        
    Returns:
        The imported module
    """
    filepath = os.path.abspath(filepath)
    module_name = os.path.basename(filepath).split(".")[0]
    
    # Determine the package name from the directory structure
    # For tests/data/patient/patient_name.py, package should be tests.data.patient
    dir_path = os.path.dirname(filepath)
    package_parts = []
    
    # Walk up from the file's directory to find the package root
    # Look for __init__.py files to determine package boundaries
    current_dir = dir_path
    while current_dir and current_dir != os.path.dirname(current_dir):
        if os.path.exists(os.path.join(current_dir, "__init__.py")):
            package_parts.insert(0, os.path.basename(current_dir))
            current_dir = os.path.dirname(current_dir)
        else:
            break
    
    # If we found package parts, set up the module with proper package context
    if package_parts:
        full_module_name = ".".join(package_parts) + "." + module_name
    else:
        full_module_name = module_name
    
    spec = importlib.util.spec_from_file_location(full_module_name, filepath)
    imported_module = importlib.util.module_from_spec(spec)
    
    # Set __package__ to enable relative imports
    if package_parts:
        imported_module.__package__ = ".".join(package_parts)
    else:
        imported_module.__package__ = None
    
    spec.loader.exec_module(imported_module)
    
    return imported_module


def camel_to_pascal(snake_str: str) -> str:
    """Convert snake_case to PascalCase."""
    components = snake_str.split('_')
    return ''.join(word.capitalize() for word in components)


def find_transformer_class(module: Any, table_name: str):
    """Find the transformer class in the module.
    
    The transformer class should follow the pattern: {PascalCase(table_name)}Transformer
    e.g., patient_identifier -> PatientIdentifierTransformer
    """
    class_name = f"{camel_to_pascal(table_name)}Transformer"
    
    if not hasattr(module, class_name):
        raise AttributeError(
            f"Module does not contain a class named '{class_name}'. "
            f"Available classes: {[name for name in dir(module) if not name.startswith('_')]}"
        )
    
    return getattr(module, class_name)


def get_resource_type_from_module_name(table_name: str) -> str:
    """Extract the resource type directory from the table name.
    
    e.g., 'patient_identifier' -> 'patient'
    """
    return table_name.split('_')[0]


def import_transformer_module(table_name: str) -> tuple[Any, Any]:
    """Dynamically import the transformer module and return the module and class.
    
    Args:
        table_name: The name of the transformer table/module (e.g., 'patient_identifier')
        
    Returns:
        Tuple of (module, transformer_class)
    """
    # Get the resource type directory from the table name
    resource_type_dir = get_resource_type_from_module_name(table_name)
    
    # Construct the path to the transformer module
    current_dir = os.path.dirname(os.path.abspath(__file__))
    transformer_path = os.path.join(
        current_dir,
        'radiant_fhir_transform_cli',
        'transform',
        'classes',
        resource_type_dir,
        f'{table_name}.py'
    )
    transformer_path = os.path.normpath(transformer_path)
    
    if not os.path.exists(transformer_path):
        raise FileNotFoundError(
            f"Transformer module not found at: {transformer_path}"
        )
    
    # Import the module
    module = dynamic_import(transformer_path)
    
    # Find the transformer class
    transformer_class = find_transformer_class(module, table_name)
    
    return module, transformer_class


def import_test_resource(table_name: str, resource_type: str) -> dict:
    """Import the RESOURCE from the test data file.
    
    The test resource is located at: tests/data/<resource_type>/<table_name>.py
    
    Args:
        table_name: The table name (e.g., 'patient_identifier')
        resource_type: The resource type in lowercase (e.g., 'patient')
        
    Returns:
        The RESOURCE dictionary
    """
    # Construct the path to the test resource file
    # Path format: tests/data/<resource_type>/<table_name>.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_resource_path = os.path.join(
        current_dir,
        'tests',
        'data',
        resource_type,
        f'{table_name}.py'
    )
    test_resource_path = os.path.normpath(test_resource_path)
    
    if not os.path.exists(test_resource_path):
        raise FileNotFoundError(
            f"Test resource file not found at: {test_resource_path}"
        )
    
    # Import the module
    module = dynamic_import(test_resource_path)
    
    # Get the RESOURCE object (it may be imported from elsewhere in the module)
    if not hasattr(module, 'RESOURCE'):
        raise AttributeError(
            f"Module at {test_resource_path} does not contain a RESOURCE object"
        )
    
    return module.RESOURCE


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Run a transformer on a test resource and display the results",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s patient_identifier
  %(prog)s appointment_participant
  %(prog)s condition_code_coding
        """
    )
    
    parser.add_argument(
        "table_name",
        help="Name of the transformer table/module (e.g., 'patient_identifier', 'appointment_participant')"
    )
    
    parser.add_argument(
        "--format",
        choices=["grid", "simple", "plain", "github", "pipe", "orgtbl", "rst", "mediawiki", "html", "latex", "latex_raw", "latex_booktabs", "tsv"],
        default="grid",
        help="Table format (default: grid)"
    )
    
    parser.add_argument(
        "--columns",
        type=str,
        help="Comma-separated list of column names to include in the output (e.g., 'patient_id,identifier_value,identifier_system'). If not provided, all columns are shown."
    )
    
    args = parser.parse_args()
    
    try:
        # Import the transformer module and get the class
        print(f"Importing transformer module: {args.table_name}")
        transformer_module, transformer_class = import_transformer_module(args.table_name)
        
        # Instantiate the transformer to get the resource_type
        transformer = transformer_class()
        resource_type = transformer.resource_type.lower()
        
        print(f"Resource type: {resource_type}")
        print(f"Transformer class: {transformer_class.__name__}")
        
        # Import the test resource from tests/data/<resource_type>/<table_name>.py
        print(f"Importing test resource from tests/data/{resource_type}/{args.table_name}.py")
        resource = import_test_resource(args.table_name, resource_type)
        
        print(f"Transforming resource (ID: {resource.get('id', 'N/A')})...")
        
        # Transform the resource
        results = transformer.transform_resource(0, resource)
        
        if not results:
            print("No results returned from transformation.")
            return 0

        # Display results using tabulate
        print(f"\nTransformation Results ({len(results)} row(s)):\n")
        
        # Convert list of dicts to list of lists for tabulate
        if results:
            all_headers = list(results[0].keys())
            
            # Filter columns if --columns option is provided
            if args.columns:
                # Parse comma-separated column names
                requested_columns = [col.strip() for col in args.columns.split(',')]
                
                # Validate that all requested columns exist
                missing_columns = [col for col in requested_columns if col not in all_headers]
                if missing_columns:
                    print(f"Warning: The following columns were not found: {', '.join(missing_columns)}", file=sys.stderr)
                    print(f"Available columns: {', '.join(all_headers)}", file=sys.stderr)
                
                # Use only the requested columns that exist
                headers = [col for col in requested_columns if col in all_headers]
                
                if not headers:
                    print("Error: None of the requested columns exist in the results.", file=sys.stderr)
                    return 1
            else:
                headers = all_headers
            
            rows = [[row.get(header, '') for header in headers] for row in results]
            
            print(tabulate(rows, headers=headers, tablefmt=args.format))
        else:
            print("No rows to display.")
        
        return 0
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except AttributeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
