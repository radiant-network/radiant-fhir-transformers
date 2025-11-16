#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert TRANSFORM_SCHEMA to ViewDefinition using test data.

This script scans transformer modules, extracts TRANSFORM_SCHEMA,
loads corresponding test data (resource and expected_output),
and generates ViewDefinitions that produce the expected output.
"""

import argparse
import importlib.util
import json
import pathlib
import re
import shutil
import sys
from typing import Any, Dict, List, Optional, Tuple

from sqlonfhir import evaluate


def load_python_module_dict(path: str, var_name: str) -> Any:
    """Import a module from a file path and return a top-level variable."""
    spec = importlib.util.spec_from_file_location("mod", path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ValueError(f"Could not load module from {path}")
    spec.loader.exec_module(module)
    if not hasattr(module, var_name):
        raise ValueError(f"{var_name} not found in {path}")
    return getattr(module, var_name)


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def snake_to_camel(name: str) -> str:
    """Convert snake_case to camelCase (FHIR field naming)."""
    parts = name.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def strip_leading_space(path: Optional[str]) -> Optional[str]:
    """Strip leading space from a FHIR path (e.g., ' image' -> 'image')."""
    if path is None:
        return None
    return path.lstrip()


def infer_resource_type_and_subtype(py_path: str) -> Tuple[str, Optional[str]]:
    """
    Infer resource_type and resource_subtype from the directory and filename.

    Assumes:
      radiant_fhir_transform_cli/transform/classes/<resource_type>/<table_name>.py

    Examples:
      .../patient/patient.py            -> ("Patient", None)
      .../patient/patient_identifier.py -> ("Patient", "identifier")
    """
    path = pathlib.Path(py_path)
    module_name = path.stem
    dir_name = path.parent.name

    # Convert snake_case directory name to PascalCase resource type
    resource_type = "".join(word.capitalize() for word in dir_name.split("_"))

    if module_name == dir_name:
        resource_subtype = None
    else:
        if module_name.startswith(dir_name + "_"):
            subtype_snake = module_name[len(dir_name) + 1 :]
        else:
            subtype_snake = module_name
        resource_subtype = subtype_snake

    return resource_type, resource_subtype


def find_test_file(
    resource_type: str, resource_subtype: Optional[str], root_dir: pathlib.Path
) -> Optional[pathlib.Path]:
    """Find the test file for a given resource type and subtype."""
    # Convert resource type to snake_case directory name
    dir_name = camel_to_snake(resource_type)
    # Test files are in tests/data/ relative to project root
    # Find project root by looking for tests/ directory
    project_root = root_dir
    while project_root.parent != project_root:
        if (project_root / "tests").exists():
            break
        project_root = project_root.parent
    
    test_dir = project_root / "tests" / "data" / dir_name

    if resource_subtype:
        test_file = test_dir / f"{dir_name}_{resource_subtype}.py"
    else:
        test_file = test_dir / f"{dir_name}.py"

    if test_file.exists():
        return test_file
    return None


def is_array_field(
    fhir_path: Optional[str], test_resource: Optional[Dict[str, Any]]
) -> bool:
    """Check if a FHIRPath points to an array field in the test resource."""
    if not fhir_path or not test_resource:
        return False

    try:
        parts = fhir_path.split(".")
        current = test_resource
        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
            elif isinstance(current, list):
                return True
            else:
                return False

        return isinstance(current, list)
    except Exception:
        return False


def is_array_in_expected_output(
    column_name: str, expected_output: Optional[List[Dict[str, Any]]]
) -> bool:
    """
    Check if a column is an array in the expected output.

    Args:
        column_name: The name of the column
        expected_output: The expected output list
    """
    if not expected_output or not column_name:
        return False

    # Check all rows to see if this column is ever a list
    # (some rows might have empty lists, others might have None)
    for row in expected_output:
        if column_name in row:
            value = row[column_name]
            # If we find at least one row where this is a list, it's an array column
            if isinstance(value, list):
                return True
    
    return False


def convert_type_to_viewdef_type(type_str: str) -> str:
    """Convert Python type to ViewDefinition type."""
    type_lower = type_str.lower() if type_str else "string"
    if type_lower in ("datetime", "date", "time"):
        return "dateTime"
    elif type_lower in ("int", "integer", "number"):
        return "integer"
    elif type_lower in ("float", "decimal"):
        return "decimal"
    elif type_lower == "boolean":
        return "boolean"
    else:
        return "string"


def convert_transform_schema_to_viewdef(
    resource_type: str,
    resource_subtype: Optional[str],
    schema: List[Dict[str, Any]],
    test_resource: Optional[Dict[str, Any]] = None,
    expected_output: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Convert TRANSFORM_SCHEMA to ViewDefinition.

    Args:
        resource_type: The FHIR resource type (e.g., "Patient")
        resource_subtype: The resource subtype (e.g., "identifier") or None
        schema: The TRANSFORM_SCHEMA list
        test_resource: Optional test resource for validation
        expected_output: Optional expected output for validation

    Returns:
        A ViewDefinition dictionary
    """
    # Build view name
    if resource_subtype:
        view_name = f"{camel_to_snake(resource_type)}_{resource_subtype}"
    else:
        view_name = camel_to_snake(resource_type)

    view: Dict[str, Any] = {
        "resource": resource_type,
        "name": view_name,
        "status": "active",
    }

    # Subtype tables need constant for UUID generation (only if they need forEach)
    # We'll set this later after determining if forEach is needed

    # Determine if we need forEach for subtype tables
    # For subtype tables, if the subtype path is an array field AND expected output has multiple rows, we need forEach
    # Check the actual fhir_path from the schema, not just the subtype name
    needs_forEach = False
    forEach_path = None
    if resource_subtype and test_resource:
        # For subtype tables, we need forEach if the field is an array
        # However, some deeply nested paths like "medicationCodeableConcept.coding" don't work well with forEach
        # when there's only 1 row - in those cases, use full paths instead
        needs_forEach_by_output = expected_output and len(expected_output) > 1
        
        # First, try to find the fhir_path from the schema that matches the subtype
        # Look for blocks with fhir_path that might be the array we're iterating over
        # Collect all candidate array paths, then choose the shortest one (base path)
        candidate_paths = []
        for block in schema:
            fhir_path = block.get("fhir_path")
            if fhir_path and not block.get("is_foreign_key", False):
                # Strip leading space
                fhir_path_stripped = strip_leading_space(fhir_path)
                # Check both the full path and the base path (first part before '.')
                # For "code.coding", the full path "code.coding" is the array
                # For "media.comment", the base path "media" is the array
                # For paths with dots, ALWAYS check base path first
                # This prevents "media.link" from being added when "media" is the array
                if "." in fhir_path_stripped:
                    base_path = fhir_path_stripped.split(".")[0]
                    if is_array_field(base_path, test_resource):
                        # Base path is an array - use it, not the full path
                        # This prevents "media.link" from being selected when "media" is the array
                        candidate_paths.append(base_path)
                        # Skip checking the full path or intermediate paths - we already found the array at the base
                        continue
                    else:
                        # Base path is NOT an array - check if full path or intermediate paths are arrays
                        # First check if the full path is an array (e.g., "code.coding" where "code" is not an array)
                        if is_array_field(fhir_path_stripped, test_resource):
                            candidate_paths.append(fhir_path_stripped)
                        else:
                            # Check intermediate paths
                            # e.g., "effectiveTiming.repeat.when" where "effectiveTiming" is not an array
                            # but "effectiveTiming.repeat" or "effectiveTiming.repeat.when" might be
                            path_parts = fhir_path_stripped.split(".")
                            for i in range(1, len(path_parts)):
                                intermediate_path = ".".join(path_parts[:i+1])
                                if is_array_field(intermediate_path, test_resource):
                                    candidate_paths.append(intermediate_path)
                                    break
                else:
                    # No dots - check if the path itself is an array
                    if is_array_field(fhir_path_stripped, test_resource):
                        candidate_paths.append(fhir_path_stripped)
        
        # Choose the shortest candidate path (prefer base paths over nested paths)
        # This ensures "media" is chosen over "media.comment" when both are candidates
        # Also deduplicate and verify all candidates are actually arrays
        subtype_fhir_path = None
        if candidate_paths:
            # Remove duplicates and verify all are actually arrays
            unique_candidates = []
            seen = set()
            for path in candidate_paths:
                # Only add if it's unique, actually an array, and not a longer path when a shorter one exists
                if path not in seen and is_array_field(path, test_resource):
                    # Additional check: if this path contains a dot and the base path is also a candidate,
                    # prefer the base path (e.g., prefer "media" over "media.link")
                    if "." in path:
                        base = path.split(".")[0]
                        if base in candidate_paths and is_array_field(base, test_resource):
                            # Base path is also a candidate and is an array - skip this longer path
                            continue
                    unique_candidates.append(path)
                    seen.add(path)
            if unique_candidates:
                # Choose the shortest path (this will prefer "media" over "media.link" if both exist)
                subtype_fhir_path = min(unique_candidates, key=len)
        
        # Use forEach if we found an array path
        # Arrays should always use forEach, regardless of row count or path structure
        if subtype_fhir_path:
            needs_forEach = True
            forEach_path = subtype_fhir_path
        elif not subtype_fhir_path:
            # Fallback: Convert snake_case to camelCase for FHIR field name
            fhir_field_name = snake_to_camel(resource_subtype)
            if is_array_field(fhir_field_name, test_resource):
                # Arrays should always use forEach
                needs_forEach = True
                forEach_path = fhir_field_name  # Use camelCase for forEach path (already stripped)
    
    # Subtype tables ALWAYS need constant for UUID generation
    if resource_subtype is not None:
        view["constant"] = [
            {
                "name": "id_uuid",
                "valueString": "uuid()",
            }
        ]

    # Collect columns from schema
    # Skip primary key blocks (handled separately)
    columns_by_path: Dict[Optional[str], List[Dict[str, Any]]] = {}
    fk_columns: List[Dict[str, Any]] = []  # Store FK columns separately

    for block in schema:
        fhir_path = block.get("fhir_path")
        is_foreign_key = block.get("is_foreign_key", False)

        # Skip primary key generation blocks (handled separately)
        if fhir_path is None and not resource_subtype:
            continue

        # Strip leading space from fhir_path for lookups and path construction
        fhir_path_stripped = strip_leading_space(fhir_path) if fhir_path else None

        for col_name, spec in block["columns"].items():
            fhir_key = spec.get("fhir_key")
            col_type = convert_type_to_viewdef_type(spec.get("type", "str"))

            # Handle primary key blocks
            if fhir_key is None:
                if fhir_path_stripped is None:
                    continue
                path_expr = fhir_path_stripped
            elif fhir_path_stripped:
                # When both fhir_path and fhir_key are present
                if fhir_path_stripped == fhir_key:
                    # If they're the same (e.g., fhir_path="id" + fhir_key="id"), just use one
                    path_expr = fhir_path_stripped
                elif "where(" in fhir_path_stripped or ".first()" in fhir_path_stripped or ".last()" in fhir_path_stripped:
                    # If fhir_path contains FHIRPath expressions, use it directly (fhir_key is likely the same)
                    # e.g., fhir_path="name.where(use='official').given.first()" -> use as-is
                    path_expr = fhir_path_stripped
                elif fhir_path_stripped.endswith("." + fhir_key) or fhir_path_stripped.endswith("/" + fhir_key):
                    # If fhir_path already ends with fhir_key, don't combine (e.g., "serviceType.text" + "text" -> "serviceType.text")
                    # This prevents double paths like "serviceType.text.text"
                    path_expr = fhir_path_stripped
                else:
                    # Combine them (e.g., fhir_path="patient" + fhir_key="display" -> "patient.display")
                    path_expr = f"{fhir_path_stripped}.{fhir_key}"
            else:
                path_expr = fhir_key

            # Convert _value to value for ViewDefinition paths
            if path_expr and path_expr.startswith("_value"):
                path_expr = path_expr.replace("_value", "value", 1)

            # Store relative path for use in forEach blocks
            relative_path = path_expr if path_expr else fhir_path_stripped

            col_def: Dict[str, Any] = {
                "name": col_name,
                "path": relative_path,
                "type": col_type,
                "_relative_path": relative_path,
                "_fhir_path": fhir_path_stripped,  # Store stripped version for lookups
                "_fhir_key": fhir_key,  # Store original fhir_key for forEach logic
                "_is_foreign_key": is_foreign_key,
            }

            # Store FK columns separately for subtype tables with forEach
            if is_foreign_key and needs_forEach:
                fk_columns.append(col_def)
            else:
                # Use stripped fhir_path as key for columns_by_path
                path_key = fhir_path_stripped
                if path_key not in columns_by_path:
                    columns_by_path[path_key] = []
                columns_by_path[path_key].append(col_def)

    # Build select blocks
    select_blocks: List[Dict[str, Any]] = []

    if needs_forEach and forEach_path:
        # Subtype table with forEach
        # First block: forEach with columns from the array (relative paths)
        # Foreign key columns should NEVER be in the forEach block - they go in the second block
        forEach_cols = []
        fk_col_name = f"{camel_to_snake(resource_type)}_id"
        
        # Add columns from the forEach path (use relative paths)
        # Collect all columns that are relative to the array elements
        # This includes columns with fhir_path matching forEach_path or starting with forEach_path + "."
        for path_key, cols in columns_by_path.items():
            for col in cols:
                # Skip foreign key columns - they ALWAYS go in the second block
                if col.get("_is_foreign_key") or col["name"] == fk_col_name:
                    continue
                
                # Determine the path for this column
                # When inside a forEach block, paths should be relative to the array element
                col_fhir_path = col.get("_fhir_path")
                col_fhir_key = col.get("_fhir_key")
                
                # Check if this column's fhir_path matches or is within the forEach path
                # For nested paths like forEach="media" and fhir_path="media.comment", strip "media." to get "comment"
                if col_fhir_path == forEach_path:
                    # This column is from the forEach array itself
                    if col_fhir_key is None:
                        # No fhir_key means we want the array element itself
                        path_to_use = "$this"
                    else:
                        # Check if fhir_key matches the last part of the fhir_path
                        # If so, we're accessing the array element itself, not a property of it
                        path_parts = col_fhir_path.split(".")
                        last_part = path_parts[-1] if path_parts else ""
                        if col_fhir_key == last_part:
                            # fhir_key matches the last part - we want the array element itself
                            path_to_use = "$this"
                        else:
                            # Has fhir_key that's different - use just the fhir_key (relative to array element)
                            # e.g., fhir_path="identifier" + fhir_key="system" -> "system" (not "identifier.system")
                            path_to_use = col_fhir_key
                            # Convert _value to value if needed
                            if path_to_use.startswith("_value"):
                                path_to_use = path_to_use.replace("_value", "value", 1)
                elif col_fhir_path and forEach_path and col_fhir_path.startswith(forEach_path + "."):
                    # Column path is nested within the forEach path
                    # e.g., forEach="media", col_fhir_path="media.comment" -> use "comment"
                    # e.g., forEach="media", col_fhir_path="media.link" -> use "link" (then add fhir_key if present)
                    remaining_path = col_fhir_path[len(forEach_path) + 1:]  # Remove "media." prefix
                    if col_fhir_key:
                        # Combine remaining path with fhir_key
                        # e.g., remaining_path="link" + fhir_key="reference" -> "link.reference"
                        path_to_use = f"{remaining_path}.{col_fhir_key}" if remaining_path else col_fhir_key
                    else:
                        path_to_use = remaining_path
                else:
                    # Column is from a different path, skip it (not part of this forEach)
                    continue
                    
                clean_col = {
                    "name": col["name"],
                    "path": path_to_use,
                    "type": col["type"],
                }
                # Check if this column is an array in the expected output
                if is_array_in_expected_output(col["name"], expected_output):
                    clean_col["collection"] = True
                forEach_cols.append(clean_col)

        # For subtype tables with forEach, the order should be:
        # 1. First block: id (from constant) and <resource_type>_id (from root resource)
        # 2. Second block: forEach with columns from the array
        # This matches the pattern in list_empty_reason_coding.py and goal_start_codeable_concept_coding.py
        
        # First block: id (from constant) and <resource_type>_id (from root resource)
        fk_col_name = f"{camel_to_snake(resource_type)}_id"
        id_fk_cols = [
            {
                "name": "id",
                "path": "%id_uuid",
                "type": "string",
            },
            {
                "name": fk_col_name,
                "path": "id",  # Path to parent resource's id field
                "type": "string",
            }
        ]
        select_blocks.append({"column": id_fk_cols})
        
        # Second block: forEach with columns from the array
        select_blocks.append(
            {
                "forEach": forEach_path,
                "column": forEach_cols,
            }
        )
    else:
        # Main table or subtype without forEach
        all_cols = []
        
        if resource_subtype:
            # For subtype tables without forEach, add FK and id columns first
            # Order: FK first, then id, then other columns
            fk_col_name = f"{camel_to_snake(resource_type)}_id"
            
            # Add foreign key column
            all_cols.append({
                "name": fk_col_name,
                "path": "id",  # Path to parent resource's id field
                "type": "string",
            })
            
            # Add id column (from constant)
            all_cols.append({
                "name": "id",
                "path": "%id_uuid",
                "type": "string",
            })
        
        # Add all other columns
        for fhir_path, cols in columns_by_path.items():
            if not cols:
                continue

            for col in cols:
                # Skip foreign key columns for subtype tables (already added above)
                if resource_subtype and col.get("_is_foreign_key"):
                    continue
                    
                clean_col = {
                    "name": col["name"],
                    "path": col["_relative_path"] if col.get("_relative_path") else col["path"],
                    "type": col["type"],
                }
                # Check if this column is an array in the expected output
                if is_array_in_expected_output(col["name"], expected_output):
                    clean_col["collection"] = True
                all_cols.append(clean_col)
        
        if all_cols:
            select_blocks.append({"column": all_cols})

    view["select"] = select_blocks
    return view


def format_python_value(value: Any, indent: int = 2, level: int = 0) -> str:
    """Format a Python value as a string with proper indentation."""
    indent_str = " " * (level * indent)

    if isinstance(value, dict):
        if not value:
            return "{}"
        items = []
        for k, v in value.items():
            key_str = json.dumps(str(k))
            val_str = format_python_value(v, indent, level + 1)
            items.append(f"{indent_str}{key_str}: {val_str}")
        return "{\n" + ",\n".join(items) + f"\n{indent_str}}}"
    elif isinstance(value, list):
        if not value:
            return "[]"
        items = []
        for item in value:
            item_str = format_python_value(item, indent, level + 1)
            items.append(f"{indent_str}{item_str}")
        return "[\n" + ",\n".join(items) + f"\n{indent_str}]"
    elif isinstance(value, bool):
        return "True" if value else "False"
    elif value is None:
        return "None"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return json.dumps(value)


def process_file(
    src_path: pathlib.Path,
    dst_path: pathlib.Path,
    root_dir: pathlib.Path,
    verbose: bool,
) -> None:
    """Process one transformer module."""
    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    # If there's no TRANSFORM_SCHEMA, just copy the file
    if "TRANSFORM_SCHEMA" not in text:
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dst_path)
        if verbose:
            print(f"[copy] {src_path} -> {dst_path} (no TRANSFORM_SCHEMA)")
        return

    # Load TRANSFORM_SCHEMA
    try:
        transform_schema = load_python_module_dict(str(src_path), "TRANSFORM_SCHEMA")
    except Exception as e:
        print(f"[error] Failed to load TRANSFORM_SCHEMA from {src_path}: {e}")
        return

    resource_type, resource_subtype = infer_resource_type_and_subtype(str(src_path))

    # Try to load test data
    test_file = find_test_file(resource_type, resource_subtype, root_dir)
    test_resource = None
    expected_output = None

    if test_file:
        try:
            # Try to load RESOURCE - it might be in a parent file
            test_resource = None
            expected_output = None
            
            # First try loading directly from the test file
            try:
                test_resource = load_python_module_dict(str(test_file), "RESOURCE")
            except (ValueError, ImportError):
                # If not found, try to find what RESOURCE is imported as using AST
                # (e.g., "from .observation_resource import RESOURCE_EFFECTIVE_TIMING as RESOURCE")
                test_resource = None
                try:
                    import ast
                    with open(test_file, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read(), filename=str(test_file))
                    
                    # Look for imports like "from .observation_resource import RESOURCE_EFFECTIVE_TIMING as RESOURCE"
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ImportFrom) and node.module:
                            # Check if it's a relative import from a resource file
                            # Handle both ".observation_resource" and "observation_resource"
                            module_name = node.module
                            if module_name.startswith("."):
                                # Relative import - remove the dot
                                module_name = module_name[1:]
                            
                            if module_name.endswith("_resource") or "resource" in module_name.lower():
                                for alias in node.names:
                                    if alias.asname == "RESOURCE" or (alias.asname is None and alias.name.endswith("RESOURCE")):
                                        # Found the import - try to load it from the resource file
                                        resource_constant_name = alias.name
                                        test_dir = test_file.parent
                                        # Try the resource file name based on the module name
                                        if module_name.endswith("_resource"):
                                            resource_file = test_dir / f"{module_name}.py"
                                        else:
                                            resource_file = test_dir / f"{test_dir.name}_resource.py"
                                        
                                        if resource_file.exists():
                                            try:
                                                test_resource = load_python_module_dict(str(resource_file), resource_constant_name)
                                                if test_resource:
                                                    break
                                            except (ValueError, ImportError):
                                                pass
                                if test_resource:
                                    break
                    if test_resource:
                        pass  # Found it via AST
                    else:
                        # Fallback: try loading from parent resource file
                        # (e.g., patient_resource.py or patient.py)
                        test_dir = test_file.parent
                        resource_file = test_dir / f"{test_dir.name}_resource.py"
                        if resource_file.exists():
                            try:
                                test_resource = load_python_module_dict(str(resource_file), "RESOURCE")
                            except (ValueError, ImportError):
                                pass
                        if not test_resource:
                            # Try just the resource type name
                            resource_file = test_dir / f"{test_dir.name}.py"
                            if resource_file.exists():
                                try:
                                    test_resource = load_python_module_dict(str(resource_file), "RESOURCE")
                                except (ValueError, ImportError):
                                    pass
                except Exception:
                    # If AST parsing fails, try fallback approach
                    test_dir = test_file.parent
                    resource_file = test_dir / f"{test_dir.name}_resource.py"
                    if resource_file.exists():
                        try:
                            test_resource = load_python_module_dict(str(resource_file), "RESOURCE")
                        except (ValueError, ImportError):
                            pass
                    if not test_resource:
                        resource_file = test_dir / f"{test_dir.name}.py"
                        if resource_file.exists():
                            try:
                                test_resource = load_python_module_dict(str(resource_file), "RESOURCE")
                            except (ValueError, ImportError):
                                pass
            
            # Load expected output from test file
            # Use ast to parse and extract EXPECTED_OUTPUT to avoid relative import issues
            try:
                import ast
                with open(test_file, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=str(test_file))
                
                # Find EXPECTED_OUTPUT assignment
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id == "EXPECTED_OUTPUT":
                                # Evaluate the value
                                try:
                                    # Use compile and eval to get the value
                                    code = compile(ast.Expression(node.value), str(test_file), "eval")
                                    expected_output = eval(code, {"__builtins__": {}}, {})
                                    break
                                except Exception:
                                    # If eval fails, try using ast.literal_eval for simple cases
                                    try:
                                        expected_output = ast.literal_eval(node.value)
                                    except Exception:
                                        pass
                                break
                        if expected_output is not None:
                            break
            except Exception as load_error:
                if verbose:
                    print(f"[warning] Could not load EXPECTED_OUTPUT from {test_file}: {load_error}")
                pass
                
        except Exception as e:
            if verbose:
                print(f"[warning] Could not load test data from {test_file}: {e}")

    # Generate ViewDefinition
    try:
        viewdef = convert_transform_schema_to_viewdef(
            resource_type, resource_subtype, transform_schema, test_resource, expected_output
        )
    except Exception as e:
        print(f"[error] Failed to generate ViewDefinition for {src_path}: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        return

    # Generate Python code
    dst_path.parent.mkdir(parents=True, exist_ok=True)

    # Extract class name from original file
    class_match = re.search(r"class\s+(\w+Transformer)\b", text)
    if class_match:
        class_name = class_match.group(1)
    else:
        # Fallback
        if resource_subtype:
            class_name = f"{resource_type}{resource_subtype.capitalize()}Transformer"
        else:
            class_name = f"{resource_type}Transformer"

    # Format ViewDefinition as Python dict
    viewdef_str = format_python_value(viewdef, indent=2)

    # Write output file
    output = f'''"""FHIR {resource_type}{" " + resource_subtype if resource_subtype else ""} transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {viewdef_str}


class {class_name}(FhirResourceTransformer):
    def __init__(self):
        super().__init__("{resource_type}", {json.dumps(resource_subtype) if resource_subtype else "None"}, VIEW_DEFINITION)
'''

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(output)

    if verbose:
        print(f"[write] {dst_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert TRANSFORM_SCHEMA to ViewDefinition"
    )
    parser.add_argument(
        "--root",
        required=True,
        help="Root directory containing transformer classes",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output directory for generated ViewDefinitions",
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Print verbose output"
    )

    args = parser.parse_args()

    root_dir = pathlib.Path(args.root).resolve()
    out_dir = pathlib.Path(args.out).resolve()

    if not root_dir.exists():
        print(f"Error: Root directory does not exist: {root_dir}")
        sys.exit(1)

    # Clean output directory
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Find all Python files
    for py_file in root_dir.rglob("*.py"):
        # Skip __pycache__
        if "__pycache__" in str(py_file):
            continue

        # Calculate relative path
        rel_path = py_file.relative_to(root_dir)
        dst_path = out_dir / rel_path

        process_file(py_file, dst_path, root_dir, args.verbose)

    print(f"Conversion complete. Output written to {out_dir}")


if __name__ == "__main__":
    main()
