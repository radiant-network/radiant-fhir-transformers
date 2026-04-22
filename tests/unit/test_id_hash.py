"""
Unit tests for FHIR component ID resolution

This module tests the ID field generation in FHIR transformers, specifically:
- uuid(): Generates random UUID4 values
- hash_row(): Generates deterministic SHA256 hashes of row data

Tests validate that:
- UUID4 generation works correctly
- Hash generation produces correct SHA256 hashes
- last_processed is excluded from hash computation for determinism
- Same data always produces the same hash
"""

import hashlib
import json
import re

import pytest

from radiant_fhir_transform_cli.transform.classes.organization import (
    OrganizationIdentifierTransformer,
)
from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientNameTransformer,
)
from tests.data.organization.organization_address import OrganizationAddressTestHelper
from tests.data.organization.organization_resource import (
    RESOURCE as ORGANIZATION_RESOURCE,
)
from tests.data.patient.patient import RESOURCE as PATIENT_RESOURCE
from tests.data.patient.patient_name import PatientNameTestHelper


def compute_expected_hash(row: dict) -> str:
    """Compute expected SHA256 hash for a row.

    The hash is computed from the row data as it exists during resolution:
    - Includes all fields
    - "id" field contains the placeholder "hash_row()"
    - "last_processed" is included (not excluded)

    Args:
        row: A row dictionary (can have resolved or placeholder id)

    Returns:
        SHA256 hash of the row data
    """
    row_for_hash = {k: v for k, v in row.items() if k != "last_processed"}
    row_for_hash["id"] = "hash_row()"
    row_str = json.dumps(row_for_hash, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(row_str.encode("utf-8")).hexdigest()


class TestFhirComponentId:
    """Tests for the _resolve_fhir_component_id method."""

    def test_uuid_generates_valid_uuid4(self):
        """Test that uuid() placeholder generates a valid UUID4."""
        transformer = OrganizationIdentifierTransformer()

        test_row = {"id": "uuid()", "organization_id": "test-org"}
        result = transformer._resolve_fhir_component_id(test_row)

        uuid_pattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        assert re.match(
            uuid_pattern, result["id"]
        ), f"ID should be UUID4 format, got: {result['id']}"

    def test_uuid_generates_different_values(self):
        """Test that uuid() generates different values on each call."""
        transformer = OrganizationIdentifierTransformer()

        results = []
        for _ in range(3):
            test_row = {"id": "uuid()", "organization_id": "test-org"}
            result = transformer._resolve_fhir_component_id(test_row)
            results.append(result["id"])

        assert len(set(results)) == 3, "Each uuid() call should generate a unique UUID"

    def test_hash_row_generates_sha256(self):
        """Test that hash_row() generates a SHA256 hash."""
        transformer = OrganizationIdentifierTransformer()

        test_row = {
            "id": "hash_row()",
            "organization_id": "test-org",
            "field1": "value1",
        }
        result = transformer._resolve_fhir_component_id(test_row)

        assert len(result["id"]) == 64, "SHA256 hash should be 64 characters"
        assert all(c in "0123456789abcdef" for c in result["id"]), "Hash should be hexadecimal"

    def test_hash_row_excludes_last_processed(self):
        """Test that last_processed is excluded from hash computation."""
        transformer = OrganizationIdentifierTransformer()

        row1 = {
            "id": "hash_row()",
            "organization_id": "test-org",
            "field1": "value1",
            "last_processed": "2024-01-01T00:00:00Z",
        }
        row2 = {
            "id": "hash_row()",
            "organization_id": "test-org",
            "field1": "value1",
            "last_processed": "2025-01-01T00:00:00Z",
        }

        result1 = transformer._resolve_fhir_component_id(row1)
        result2 = transformer._resolve_fhir_component_id(row2)

        assert (
            result1["id"] == result2["id"]
        ), "Hash should be the same regardless of last_processed value"

    def test_hash_row_is_deterministic(self):
        """Test that same row data always produces the same hash."""
        transformer = OrganizationIdentifierTransformer()

        test_row = {
            "id": "hash_row()",
            "organization_id": "test-org",
            "field1": "value1",
            "field2": "value2",
        }

        results = []
        for _ in range(3):
            row_copy = test_row.copy()
            result = transformer._resolve_fhir_component_id(row_copy)
            results.append(result["id"])

        assert len(set(results)) == 1, "Same data should always produce the same hash"

    def test_hash_row_with_actual_transformer_output(self):
        """Test hash computation against actual transformer output."""
        transformer = OrganizationIdentifierTransformer()

        result = transformer.transform_resources([ORGANIZATION_RESOURCE])

        assert len(result) > 0, "Should have at least one row"

        for row in result:
            expected_hash = compute_expected_hash(row)
            assert (
                row["id"] == expected_hash
            ), f"ID should match computed hash. Expected: {expected_hash}, Got: {row['id']}"

    @pytest.mark.parametrize(
        "test_helper_cls",
        [
            (OrganizationAddressTestHelper),
            (PatientNameTestHelper),
        ],
    )
    def test_hash_row_with_multiple_resources(self, test_helper_cls):
        """Test hash generation with multiple resources."""
        test_helper = test_helper_cls()
        resource_type = test_helper.resource_type

        # Instantiate transformer class based on resource type
        resource_type = test_helper_cls.resource_type
        resource_component = test_helper.resource_component

        cls = test_helper_cls.transformer

        transformer = cls()

        assert test_helper.expected_table_name == transformer.table_name

        # Transform
        result = transformer.transform_resource(0, test_helper.resource)

        for row in result:
            expected_hash = compute_expected_hash(row)
            assert row["id"] == expected_hash, f"ID should match computed hash"
