#!/usr/bin/env python3
"""Test a ViewDefinition against expected output."""

import ast
import re
import sys
from pathlib import Path

from sqlonfhir import evaluate


def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def load_expected_output(test_file: Path):
    """Load EXPECTED_OUTPUT from test file using AST."""
    with open(test_file, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=str(test_file))
    
    expected_output = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "EXPECTED_OUTPUT":
                    try:
                        code = compile(ast.Expression(node.value), str(test_file), "eval")
                        expected_output = eval(code, {"__builtins__": {}}, {})
                        break
                    except Exception:
                        try:
                            expected_output = ast.literal_eval(ast.unparse(node.value))
                        except Exception:
                            pass
                    break
            if expected_output is not None:
                break
    
    return expected_output


def load_resource(resource_file: Path):
    """Load RESOURCE from resource file using AST to avoid import issues."""
    with open(resource_file, "r", encoding="utf-8") as f:
        content = f.read()
        tree = ast.parse(content, filename=str(resource_file))
    
    # Try to find RESOURCE assignment
    resource = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "RESOURCE":
                    try:
                        code = compile(ast.Expression(node.value), str(resource_file), "eval")
                        resource = eval(code, {"__builtins__": {}}, {})
                        break
                    except Exception:
                        try:
                            resource = ast.literal_eval(node.value)
                        except Exception:
                            # If it's a variable reference, try to find it
                            if isinstance(node.value, ast.Name):
                                # Look for the variable in the file
                                for n in ast.walk(tree):
                                    if isinstance(n, ast.Assign):
                                        for t in n.targets:
                                            if isinstance(t, ast.Name) and t.id == node.value.id:
                                                try:
                                                    code = compile(ast.Expression(n.value), str(resource_file), "eval")
                                                    resource = eval(code, {"__builtins__": {}}, {})
                                                    break
                                                except Exception:
                                                    pass
                    break
            if resource is not None:
                break
    
    # If AST parsing fails, try import with sys.path manipulation
    if resource is None:
        import importlib.util
        import sys
        parent_dir = str(resource_file.parent)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)
        try:
            spec = importlib.util.spec_from_file_location("mod", resource_file)
            module = importlib.util.module_from_spec(spec)
            if spec.loader is None:
                raise ValueError(f"Could not load module from {resource_file}")
            spec.loader.exec_module(module)
            if hasattr(module, "RESOURCE"):
                resource = getattr(module, "RESOURCE")
        except Exception as e:
            raise ValueError(f"Could not load RESOURCE from {resource_file}: {e}")
    
    if resource is None:
        raise ValueError(f"RESOURCE not found in {resource_file}")
    return resource


def load_viewdef(viewdef_file: Path):
    """Load VIEW_DEFINITION from generated file."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", viewdef_file)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise ValueError(f"Could not load module from {viewdef_file}")
    spec.loader.exec_module(module)
    if not hasattr(module, "VIEW_DEFINITION"):
        raise ValueError(f"VIEW_DEFINITION not found in {viewdef_file}")
    return getattr(module, "VIEW_DEFINITION")


def strip_resource_type_from_foreign_keys(rows):
    """
    Post-process rows to strip resource type prefixes from foreign key and reference values.
    
    For example, "Patient/123" becomes "123".
    Handles:
    - Foreign key columns (ending with "_id")
    - Reference columns (ending with "_reference")
    """
    if not rows:
        return rows
    
    # Common FHIR resource types that might appear in references
    resource_types = [
        "Patient", "Practitioner", "Organization", "Encounter", "Condition",
        "Observation", "Procedure", "Medication", "MedicationRequest",
        "ServiceRequest", "DiagnosticReport", "AllergyIntolerance", "CarePlan",
        "CareTeam", "Goal", "Immunization", "Location", "RelatedPerson",
        "Appointment", "Coverage", "DocumentReference", "List", "Specimen",
        "BodyStructure", "Consent", "Provenance", "RequestGroup", "Binary"
    ]
    
    processed_rows = []
    for row in rows:
        processed_row = {}
        for key, value in row.items():
            # Check if this is a foreign key column (ends with _id) or reference column (ends with _reference)
            # and the value is a string that looks like "ResourceType/ID"
            if isinstance(value, str) and "/" in value:
                should_process = (
                    key.endswith("_id") or 
                    key.endswith("_reference") or
                    "_reference" in key
                )
                
                if should_process:
                    # Try to strip resource type prefix
                    parts = value.split("/", 1)
                    if len(parts) == 2 and parts[0] in resource_types:
                        processed_row[key] = parts[1]  # Just the ID part
                    else:
                        processed_row[key] = value
                else:
                    processed_row[key] = value
            else:
                processed_row[key] = value
        processed_rows.append(processed_row)
    
    return processed_rows


def normalize_output(rows):
    """Normalize output for comparison (sort columns, handle None)."""
    if not rows:
        return []
    
    # Sort columns in each row
    normalized = []
    for row in rows:
        normalized.append({k: row.get(k) for k in sorted(row.keys())})
    
    return normalized


def normalize_value(value, column_name):
    """
    Normalize a value for comparison:
    1. Treat empty lists [] and None as equivalent
    2. For reference columns, strip resource type prefixes (e.g., "Patient/123" -> "123")
    
    Returns:
    - None for both None and []
    - Stripped reference values for reference columns
    - Original value otherwise
    """
    # Normalize empty list to None (treat as equivalent)
    if value == [None]:
        value = None
    # Normalize empty list to None (treat as equivalent)
    if value == []:
        value = None
    
    if value is None:
        return None
    
    # Only normalize reference columns
    is_reference_column = (
        column_name.endswith("_id") or 
        column_name.endswith("_reference") or
        "_reference" in column_name
    )
    
    if not is_reference_column:
        return value
    
    # If it's a string with a "/", try to strip the prefix
    if isinstance(value, str) and "/" in value:
        parts = value.split("/", 1)
        if len(parts) == 2:
            # Check if first part looks like a resource type
            # Resource types can be PascalCase (e.g., "ServiceRequest") or camelCase (e.g., "serviceRequest")
            prefix = parts[0]
            if prefix and prefix.replace("_", "").isalnum():
                # Check if it's PascalCase (starts with uppercase) or camelCase (starts with lowercase but has uppercase later)
                is_pascal_case = prefix[0].isupper()
                is_camel_case = prefix[0].islower() and any(c.isupper() for c in prefix[1:])
                if is_pascal_case or is_camel_case:
                    return parts[1]  # Return just the ID part
    
    return value


def compare_outputs(actual, expected):
    """
    Compare actual and expected outputs with normalization:
    - Treats empty lists [] and None as equivalent
    - Strips resource type prefixes from reference columns (e.g., "Patient/123" -> "123")
    
    Returns:
        (is_match: bool, message: str, differences: list)
        differences is a list of dicts with keys: row, column, actual_value, expected_value
    """
    actual_norm = normalize_output(actual)
    expected_norm = normalize_output(expected)
    
    # Remove 'id' column from both actual and expected (UUIDs can't be compared)
    for row in actual_norm:
        row.pop("id", None)
    for row in expected_norm:
        row.pop("id", None)
    
    differences = []
    
    if len(actual_norm) != len(expected_norm):
        return False, f"Row count mismatch: {len(actual_norm)} vs {len(expected_norm)}", differences
    
    for i, (act_row, exp_row) in enumerate(zip(actual_norm, expected_norm)):
        act_keys = set(act_row.keys())
        exp_keys = set(exp_row.keys())
        
        if act_keys != exp_keys:
            # Find which columns are different
            only_in_actual = act_keys - exp_keys
            only_in_expected = exp_keys - act_keys
            common_keys = act_keys & exp_keys
            
            mismatch_msg = f"Row {i}: Column mismatch."
            if only_in_actual:
                mismatch_msg += f" Only in actual: {sorted(only_in_actual)}."
            if only_in_expected:
                mismatch_msg += f" Only in expected: {sorted(only_in_expected)}."
            
            # Still compare common columns
            for key in common_keys:
                act_value = normalize_value(act_row[key], key)
                exp_value = normalize_value(exp_row[key], key)
                
                if act_value != exp_value:
                    differences.append({
                        "row": i,
                        "column": key,
                        "actual_value": act_value,
                        "expected_value": exp_value
                    })
            
            # Add column mismatch info to differences
            if only_in_actual:
                for key in only_in_actual:
                    differences.append({
                        "row": i,
                        "column": key,
                        "actual_value": act_row[key],
                        "expected_value": "<column not in expected>"
                    })
            if only_in_expected:
                for key in only_in_expected:
                    differences.append({
                        "row": i,
                        "column": key,
                        "actual_value": "<column not in actual>",
                        "expected_value": exp_row[key]
                    })
            
            return False, mismatch_msg, differences
        
        # Columns match, compare values
        for key in act_row.keys():
            # Normalize values in both actual and expected
            # This handles: empty list/None equivalence and reference prefix stripping
            act_value = normalize_value(act_row[key], key)
            exp_value = normalize_value(exp_row[key], key)
            
            if act_value != exp_value:
                differences.append({
                    "row": i,
                    "column": key,
                    "actual_value": act_value,
                    "expected_value": exp_value
                })
    
    if differences:
        return False, f"Found {len(differences)} difference(s)", differences
    
    return True, "Match", differences


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_viewdef.py <viewdef_file>")
        sys.exit(1)
    
    viewdef_file = Path(sys.argv[1])
    if not viewdef_file.exists():
        print(f"Error: {viewdef_file} does not exist")
        sys.exit(1)
    
    # Load ViewDefinition first to get the resource type and name
    print(f"Loading ViewDefinition from: {viewdef_file}")
    viewdef = load_viewdef(viewdef_file)
    
    # Get resource type from ViewDefinition (e.g., "RelatedPerson" -> "related_person")
    resource_type_fhir = viewdef.get("resource", "")
    resource_type = camel_to_snake(resource_type_fhir) if resource_type_fhir else ""
    
    # Get view name (e.g., "related_person_name")
    view_name = viewdef.get("name", "")
    
    # Infer test file path
    # The view name is typically: <resource_type>_<subtype> or just <resource_type>
    # e.g., "related_person_name" or "patient"
    if not resource_type:
        # Fallback: try to extract from view name
        parts = view_name.split("_", 1)
        if len(parts) == 2:
            resource_type, subtype = parts
            test_file = Path("tests/data") / resource_type / f"{resource_type}_{subtype}.py"
        else:
            resource_type = parts[0]
            test_file = Path("tests/data") / resource_type / f"{resource_type}.py"
    else:
        # Use resource type from ViewDefinition
        # Check if view name matches resource type (for main tables) or has a subtype
        if view_name == resource_type:
            # Main table (e.g., "patient" -> "patient.py")
            test_file = Path("tests/data") / resource_type / f"{resource_type}.py"
        elif view_name.startswith(resource_type + "_"):
            # Subtype table (e.g., "related_person_name" -> "related_person_name.py")
            test_file = Path("tests/data") / resource_type / f"{view_name}.py"
        else:
            # Fallback: use view name as-is
            test_file = Path("tests/data") / resource_type / f"{view_name}.py"
    
    if not test_file.exists():
        print(f"Error: Could not find test file for {viewdef_file}")
        print(f"View name: {view_name}")
        print(f"Tried: {test_file}")
        sys.exit(1)
    
    print(f"Loading test data from: {test_file}")
    expected_output = load_expected_output(test_file)
    
    # Find resource file - prefer _resource.py files
    resource_file = test_file.parent / f"{resource_type}_resource.py"
    if not resource_file.exists():
        resource_file = test_file.parent / f"{resource_type}.py"
    if not resource_file.exists():
        # Try parent directory
        resource_file = test_file.parent.parent / f"{resource_type}_resource.py"
    if not resource_file.exists():
        resource_file = test_file.parent.parent / f"{resource_type}.py"
    
    if not resource_file.exists():
        print(f"Error: Could not find resource file")
        sys.exit(1)
    
    print(f"Loading resource from: {resource_file}")
    resource = load_resource(resource_file)
    
    # Evaluate ViewDefinition
    print("\nEvaluating ViewDefinition...")
    try:
        actual_output = evaluate(resources=[resource], view_definition=viewdef)
        print(f"Actual output: {len(actual_output)} rows")
    except Exception as e:
        print(f"Error evaluating ViewDefinition: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Post-process: strip resource type prefixes from foreign key values
    actual_output = strip_resource_type_from_foreign_keys(actual_output)
    
    # Compare
    print(f"Expected output: {len(expected_output)} rows")
    print("\nComparing outputs...")
    match, message, differences = compare_outputs(actual_output, expected_output)
    
    if match:
        print("✓ PASS: Output matches expected!")
    else:
        print(f"✗ FAIL: {message}")
        
        # Print detailed differences
        if differences:
            print("\n" + "=" * 80)
            print("DETAILED DIFFERENCES:")
            print("=" * 80)
            for diff in differences:
                print(f"\nRow {diff['row']}, Column '{diff['column']}':")
                print(f"  Actual:   {repr(diff['actual_value'])}")
                print(f"  Expected: {repr(diff['expected_value'])}")
            print("=" * 80)
        
        print("\nFull Actual output:")
        import json
        print(json.dumps(actual_output, indent=2))
        print("\nFull Expected output:")
        print(json.dumps(expected_output, indent=2))
        sys.exit(1)

