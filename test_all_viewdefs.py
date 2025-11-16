#!/usr/bin/env python3
"""Test all ViewDefinitions in a directory (recursively)."""

import subprocess
import sys
from pathlib import Path


def test_viewdef(viewdef_file: Path) -> tuple[bool, str]:
    """Test a single ViewDefinition and return (success, message)."""
    try:
        result = subprocess.run(
            [sys.executable, "test_viewdef.py", str(viewdef_file)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        output = result.stdout + result.stderr
        
        if "✓ PASS" in output:
            return True, "PASS"
        elif "✗ FAIL" in output:
            # Extract the failure message
            lines = output.split("\n")
            for line in lines:
                if "✗ FAIL" in line:
                    return False, line.replace("✗ FAIL: ", "")
            return False, "FAIL (unknown reason)"
        elif "Error" in output or result.returncode != 0:
            # Try to extract error message
            lines = output.split("\n")
            for line in lines:
                if "Error:" in line or "Exception:" in line:
                    return False, line.strip()
            return False, f"Error: {result.returncode}"
        else:
            return False, f"Error: {result.returncode}"
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, f"Exception: {e}"


def find_viewdef_files(directory: Path, recursive: bool = True) -> list[Path]:
    """Find all ViewDefinition files in a directory."""
    viewdef_files = []
    
    if recursive:
        # Recursively find all Python files
        all_py_files = sorted(directory.rglob("*.py"))
    else:
        # Only files in the immediate directory
        all_py_files = sorted(directory.glob("*.py"))
    
    # Filter to only files that have VIEW_DEFINITION
    for py_file in all_py_files:
        # Skip certain files
        if py_file.name in ("__init__.py", "base.py", "raw_fhir.py"):
            continue
        
        try:
            with open(py_file, "r") as f:
                content = f.read()
                if "VIEW_DEFINITION" in content:
                    viewdef_files.append(py_file)
        except Exception:
            pass
    
    return viewdef_files


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_all_viewdefs.py <directory> [--no-recursive]")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    recursive = "--no-recursive" not in sys.argv
    
    if not directory.exists():
        print(f"Error: {directory} does not exist")
        sys.exit(1)
    
    # Find all transformer files
    viewdef_files = find_viewdef_files(directory, recursive=recursive)
    
    if not viewdef_files:
        print(f"No transformer files with VIEW_DEFINITION found in {directory}")
        sys.exit(1)
    
    print(f"Testing {len(viewdef_files)} transformers...\n")
    
    passed = 0
    failed = 0
    failed_files = []
    
    for viewdef_file in viewdef_files:
        # Show relative path for clarity
        rel_path = viewdef_file.relative_to(directory)
        success, message = test_viewdef(viewdef_file)
        
        if success:
            print(f"✓ {rel_path}: PASS")
            passed += 1
        else:
            print(f"✗ {rel_path}: {message}")
            failed += 1
            failed_files.append((rel_path, message))
    
    print(f"\nSummary: {passed} passed, {failed} failed out of {len(viewdef_files)} total")
    
    if failed > 0 and len(failed_files) <= 20:
        print("\nFailed files:")
        for file_path, msg in failed_files:
            print(f"  - {file_path}: {msg}")

