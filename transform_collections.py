#!/usr/bin/env python3
"""
Script to transform ViewDefinitions by replacing collection: True columns
with nested forEach blocks.

This script:
1. Scans transform modules for VIEW_DEFINITION
2. Finds columns with collection: True
3. Transforms them into nested select blocks with forEach
4. Outputs transformed modules to a parallel directory structure
"""

import ast
import shutil
import re
import sys
import importlib.util
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Common FHIR object structures and their fields
FHIR_OBJECT_FIELDS = {
    ".coding": ["system", "code", "display"],
    ".identifier": ["use", "type", "system", "value", "period"],
    ".reference": ["reference", "type", "display", "identifier"],
    ".period": ["start", "end"],
    ".quantity": ["value", "comparator", "unit", "system", "code"],
    ".range": ["low", "high"],
    ".ratio": ["numerator", "denominator"],
    ".sampledData": [
        "origin",
        "period",
        "factor",
        "lowerLimit",
        "upperLimit",
        "dimensions",
        "data",
    ],
    ".address": [
        "use",
        "type",
        "text",
        "line",
        "city",
        "district",
        "state",
        "postalCode",
        "country",
        "period",
    ],
    ".contactPoint": ["system", "value", "use", "rank", "period"],
    ".humanName": ["use", "text", "family", "given", "prefix", "suffix", "period"],
    ".codeableConcept": ["coding", "text"],
    ".timing": ["event", "repeat", "code"],
    ".attachment": [
        "contentType",
        "language",
        "data",
        "url",
        "size",
        "hash",
        "title",
        "creation",
    ],
}


def navigate_fhir_path(resource: Dict[str, Any], path: str) -> Any:
    """Navigate a FHIRPath expression in a resource dict.
    
    Returns the value at the path, or None if not found.
    """
    parts = path.split(".")
    current = resource
    
    for part in parts:
        if isinstance(current, list):
            # If we hit a list, we need to check the first element
            if len(current) > 0 and isinstance(current[0], dict):
                current = current[0].get(part)
            else:
                return None
        elif isinstance(current, dict):
            current = current.get(part)
        else:
            return None
        
        if current is None:
            return None
    
    return current


def get_test_resource(transform_module_path: Path) -> Optional[Dict[str, Any]]:
    """Find and load the test resource for a transform module.
    
    Given a transform module like patient_name.py, extracts the resource type
    (patient) and loads tests/data/patient/patient_resource.py
    """
    # Extract resource type from module filename
    # e.g., patient_name.py -> patient
    module_name = transform_module_path.stem  # e.g., "patient_name"
    
    # Split by underscore and take first part as resource type
    # This handles cases like patient_name, observation_component, etc.
    resource_type = module_name.split("_")[0]
    
    # Find project root (directory containing "tests")
    project_root = transform_module_path
    while project_root.parent != project_root:
        if (project_root / "tests").exists():
            break
        project_root = project_root.parent
    
    # Build test resource path: tests/data/<resource_type>/<resource_type>_resource.py
    test_resource_path = project_root / "tests" / "data" / resource_type / f"{resource_type}_resource.py"
    
    if not test_resource_path.exists():
        return None
    
    try:
        # Load the module
        spec = importlib.util.spec_from_file_location("test_resource", str(test_resource_path))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Get RESOURCE variable
        if hasattr(module, "RESOURCE"):
            return module.RESOURCE
        return None
    except Exception as e:
        print(f"Warning: Could not load test resource from {test_resource_path}: {e}")
        return None


def get_object_fields_for_path(
    path: str,
    resource: Optional[Dict[str, Any]] = None,
    forEach_context: Optional[str] = None,
) -> Optional[List[str]]:
    """Determine what fields to extract for a given FHIRPath.
    
    Args:
        path: The FHIRPath to the collection (relative to forEach_context if provided)
        resource: The test resource to inspect (optional)
        forEach_context: The current forEach path if in a nested context
    
    Returns None if this is a list of literals (should use $this).
    Returns a list of field names if this is a list of objects.
    """
    # If we have a resource, inspect it
    if resource:
        try:
            # Navigate to the forEach context first (if any)
            if forEach_context:
                # Navigate to the forEach context (which should be an array)
                context_value = navigate_fhir_path(resource, forEach_context)
                if context_value is None or not isinstance(context_value, list) or len(context_value) == 0:
                    # Can't inspect, fall through to heuristics
                    pass
                else:
                    # Get the first element of the forEach context
                    context_element = context_value[0]
                    if not isinstance(context_element, dict):
                        # Context element is not a dict, can't navigate further
                        pass
                    else:
                        # Now navigate the relative path from within the context element
                        collection = navigate_fhir_path(context_element, path)
                        if collection is not None:
                            # Check if it's a list
                            if isinstance(collection, list) and len(collection) > 0:
                                first_item = collection[0]
                                # If first item is a dict, it's a list of objects
                                if isinstance(first_item, dict):
                                    # Return the keys of the first object as fields
                                    return list(first_item.keys())
                                else:
                                    # It's a list of literals
                                    return None
            else:
                # No forEach context, navigate from root
                collection = navigate_fhir_path(resource, path)
                if collection is not None:
                    # Check if it's a list
                    if isinstance(collection, list) and len(collection) > 0:
                        first_item = collection[0]
                        # If first item is a dict, it's a list of objects
                        if isinstance(first_item, dict):
                            # Return the keys of the first object as fields
                            return list(first_item.keys())
                        else:
                            # It's a list of literals
                            return None
        except Exception as e:
            # If navigation fails, fall through to heuristics
            pass
    
    # Fallback: Check if path ends with a known object type
    for suffix, fields in FHIR_OBJECT_FIELDS.items():
        if path.endswith(suffix):
            return fields
    
    # If path contains dots, it's likely an object path
    # But we don't know the fields, so we'll need to infer or use a default
    if "." in path:
        # For unknown object paths, we can't determine fields automatically
        # This will need manual handling or we use a heuristic
        # For now, return None to use $this (user can manually fix)
        return None
    
    # Simple field name (like "given") - likely a list of literals
    return None


def extract_view_definition(module_path: Path) -> Optional[Dict[str, Any]]:
    """Extract VIEW_DEFINITION from a Python module file."""
    try:
        with open(module_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        tree = ast.parse(content, filename=str(module_path))
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "VIEW_DEFINITION":
                        # Convert AST to dict
                        if isinstance(node.value, ast.Dict):
                            return ast.literal_eval(node.value)
        return None
    except Exception as e:
        print(f"Error reading {module_path}: {e}")
        return None


def has_view_definition(module_path: Path) -> bool:
    """Check if a module contains VIEW_DEFINITION."""
    return extract_view_definition(module_path) is not None


def transform_collection_column(
    col: Dict[str, Any],
    forEach_context: Optional[str] = None,
    resource: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Transform a collection column into a nested select block.
    
    Args:
        col: Column dict with collection: True
        forEach_context: The current forEach path (if any) for relative paths
        resource: The test resource to inspect for collection type
    
    Returns:
        A select block dict with forEach and columns
    """
    col_path = col.get("path", "")
    col_name = col.get("name", "")
    col_type = col.get("type", "string")
    
    # Determine the forEach path
    # If we're in a forEach context, the path is relative to that
    if forEach_context:
        # Path is already relative to forEach context
        forEach_path = col_path
    else:
        # Path is relative to root resource
        forEach_path = col_path
    
    # Determine if this is a list of literals or objects
    object_fields = get_object_fields_for_path(col_path, resource, forEach_context)
    
    if object_fields is None:
        # List of literals - use $this
        return {
            "forEach": forEach_path,
            "column": [
                {
                    "name": col_name,
                    "path": "$this",
                    "type": col_type,
                }
            ],
        }
    else:
        # List of objects - extract fields
        # Generate column names based on the original column name
        base_name = col_name
        columns = []
        for field in object_fields:
            field_name = f"{base_name}_{field}"
            columns.append({
                "name": field_name,
                "path": field,
                "type": col_type,
            })
        
        return {
            "forEach": forEach_path,
            "column": columns,
        }


def transform_view_definition(
    view_def: Dict[str, Any],
    resource: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Transform a ViewDefinition by replacing collection columns with nested selects.
    
    Args:
        view_def: The ViewDefinition to transform
        resource: Optional test resource to inspect for collection types
    """
    view_def = view_def.copy()
    
    if "select" not in view_def:
        return view_def
    
    def transform_select_item(
        item: Dict[str, Any],
        forEach_context: Optional[str] = None,
        resource: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Recursively transform a select item."""
        item = item.copy()
        
        # Get current forEach context
        current_forEach = item.get("forEach") or forEach_context
        
        # Process columns
        if "column" in item:
            columns = item["column"]
            collection_cols = []
            non_collection_cols = []
            
            for col in columns:
                if col.get("collection") is True:
                    collection_cols.append(col)
                else:
                    non_collection_cols.append(col)
            
            # Update columns list (remove collection columns)
            item["column"] = non_collection_cols
            
            # Transform collection columns into nested selects
            if collection_cols:
                nested_selects = []
                for col in collection_cols:
                    nested_select = transform_collection_column(
                        col, current_forEach, resource
                    )
                    nested_selects.append(nested_select)
                
                # Add nested selects to the item
                if "select" in item:
                    # Merge with existing selects
                    item["select"] = item["select"] + nested_selects
                else:
                    item["select"] = nested_selects
        
        # Recursively process nested selects
        if "select" in item:
            item["select"] = [
                transform_select_item(sub_item, current_forEach, resource)
                for sub_item in item["select"]
            ]
        
        return item
    
    # Transform all select items
    view_def["select"] = [
        transform_select_item(item, resource=resource) for item in view_def["select"]
    ]
    
    return view_def


def format_view_definition_as_python(view_def: Dict[str, Any], indent: int = 0) -> str:
    """Format a ViewDefinition dict as Python code."""
    indent_str = "    " * indent
    lines = ["{"]
    
    def format_value(val: Any) -> str:
        """Format a value, ensuring strings use double quotes."""
        if isinstance(val, str):
            # Escape double quotes and wrap in double quotes
            escaped = val.replace("\\", "\\\\").replace('"', "\\\"")
            return f"\"{escaped}\""
        elif isinstance(val, bool):
            return "True" if val else "False"
        elif val is None:
            return "None"
        else:
            return repr(val)
    
    for key, value in view_def.items():
        key_str = f"\"{key}\""
        if isinstance(value, dict):
            value_str = format_view_definition_as_python(value, indent + 1)
            lines.append(f"{indent_str}    {key_str}: {value_str},")
        elif isinstance(value, list):
            lines.append(f"{indent_str}    {key_str}: [")
            for item in value:
                if isinstance(item, dict):
                    item_str = format_view_definition_as_python(item, indent + 2)
                    lines.append(f"{indent_str}        {item_str},")
                else:
                    item_str = format_value(item)
                    lines.append(f"{indent_str}        {item_str},")
            lines.append(f"{indent_str}    ],")
        else:
            value_str = format_value(value)
            lines.append(f"{indent_str}    {key_str}: {value_str},")
    
    lines.append(f"{indent_str}}}")
    return "\n".join(lines)


def write_transformed_module(
    source_path: Path,
    dest_path: Path,
    transformed_view_def: Dict[str, Any],
):
    """Write a transformed module file."""
    # Read original file
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find VIEW_DEFINITION assignment using regex
    # Match: VIEW_DEFINITION = { ... }
    pattern = r"VIEW_DEFINITION\s*=\s*\{"
    match = re.search(pattern, content)
    
    if not match:
        # Fallback: just copy the file
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, dest_path)
        return
    
    # Find the start and end of the VIEW_DEFINITION dict
    start_pos = match.start()
    
    # Find matching closing brace
    brace_count = 0
    in_string = False
    string_char = None
    i = match.end() - 1  # Start from the opening brace
    
    while i < len(content):
        char = content[i]
        
        if not in_string:
            if char in ("\"", "'"):
                in_string = True
                string_char = char
            elif char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0:
                    end_pos = i + 1
                    break
        else:
            if char == string_char and content[i-1] != '\\':
                in_string = False
                string_char = None
        
        i += 1
    else:
        # Couldn't find matching brace, just copy file
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, dest_path)
        return
    
    # Replace VIEW_DEFINITION
    before = content[:start_pos]
    after = content[end_pos:]
    
    # Format the transformed view definition
    formatted_def = format_view_definition_as_python(transformed_view_def)
    
    new_content = before + "VIEW_DEFINITION = " + formatted_def + after
    
    # Write transformed file
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def process_directory(source_dir: Path, dest_dir: Path):
    """Process all Python files in a directory recursively."""
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)
    
    # Find all Python files
    python_files = list(source_dir.rglob("*.py"))
    
    for source_file in python_files:
        # Calculate relative path
        rel_path = source_file.relative_to(source_dir)
        dest_file = dest_dir / rel_path
        
        if has_view_definition(source_file):
            # Transform the module
            print(f"Transforming: {rel_path}")
            view_def = extract_view_definition(source_file)
            if view_def:
                # Try to load test resource
                resource = get_test_resource(source_file)
                if resource:
                    print(f"  Loaded test resource for inspection")
                else:
                    print(f"  Warning: Could not load test resource, using heuristics")
                
                transformed = transform_view_definition(view_def, resource)
                write_transformed_module(source_file, dest_file, transformed)
        else:
            # Copy file as-is
            print(f"Copying (no VIEW_DEFINITION): {rel_path}")
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest_file)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Transform ViewDefinitions by replacing collection columns with nested forEach blocks"
    )
    parser.add_argument(
        "--source",
        type=str,
        default="radiant_fhir_transform_cli/transform/classes",
        help="Source directory containing transform modules",
    )
    parser.add_argument(
        "--dest",
        type=str,
        required=True,
        help="Destination directory for transformed modules",
    )
    
    args = parser.parse_args()
    
    source_path = Path(args.source)
    dest_path = Path(args.dest)
    
    if not source_path.exists():
        print(f"Error: Source directory does not exist: {source_path}")
        exit(1)
    
    print(f"Processing modules from {source_path} to {dest_path}")
    process_directory(source_path, dest_path)
    print("Done!")

