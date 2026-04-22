"""
Unit tests for FHIR resource transformers

This module contains unit tests that validate the functionality of FHIR
resource transformers by using test helper classes defined in the
`tests.data.test_helpers`.

The tests ensure that the transformer classes correctly transform the
FHIR resource data into the expected output.

Tests include:
    - Instantiating test helper classes.
    - Dynamically loading the corresponding transformer class based on the
      resource type.
    - Transforming the resource using the transformer.
    - Validating the transformed output against the expected result.

"""

import hashlib
import json
from datetime import datetime
from pprint import pprint

import pandas as pd
import pytest

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationExtensionTransformer,
)
from radiant_fhir_transform_cli.transform.classes.patient.patient_address import (
    PatientAddressTransformer,
)
from radiant_fhir_transform_cli.transform.classes.raw_fhir import (
    RawFhirResourceTransformer,
)
from tests.data import test_helpers
from tests.data.appointment.appointment_participant import (
    AppointmentParticipantTestHelper,
)

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 0)


def normalize_reference_values(value):
    """
    Recursively normalize reference values by removing resource type prefixes.

    Handles:
    - None: returns None
    - str: applies split("/")[-1] if "/" is in the string
    - dict: recursively processes values for keys ending in "_reference"
    - list: recursively processes each element

    Args:
        value: The value to normalize (can be None, str, dict, or list)

    Returns:
        Normalized value with reference prefixes removed
    """
    if value is None:
        return None

    if isinstance(value, str):
        # If string contains "/", split and return the last part
        if "/" in value:
            return value.split("/")[-1]
        return value

    if isinstance(value, dict):
        # Create a new dict and process each key-value pair
        result = {}
        for key, val in value.items():
            if key.endswith("_reference"):
                # This is a reference field - normalize the value
                result[key] = normalize_reference_values(val)
            else:
                # Recursively process the value (might be a nested dict/list)
                result[key] = val
        return result

    if isinstance(value, list):
        # Recursively process each element in the list
        return [normalize_reference_values(item) for item in value]

    # For other types (int, float, bool, etc.), return as-is
    return value


def serialize_complex_types(value):
    if value is None:
        return None

    if isinstance(value, dict):
        # Create a new dict and process each key-value pair
        result = {}
        for key, val in value.items():
            if isinstance(val, (dict, list)):
                result[key] = json.dumps(val, default=str, sort_keys=True, separators=(",", ":"))
            else:
                result[key] = val
        return result

    if isinstance(value, list):
        # Recursively process each element in the list
        return [serialize_complex_types(item) for item in value]

    # For other types (int, float, bool, etc.), return as-is
    return value


@pytest.mark.parametrize("test_helper_cls", list(test_helpers))
def test_transformers(test_helper_cls):
    """
    Test every transformer class. Use test helper classes in tests.data
    """
    # Instantiate test helper class
    test_helper = test_helper_cls()

    # Instantiate transformer class based on resource type
    resource_type = test_helper_cls.resource_type
    resource_component = test_helper.resource_component

    cls = test_helper_cls.transformer

    transformer = cls()

    assert test_helper.expected_table_name == transformer.table_name

    # Transform
    actual = transformer.transform_resource(0, test_helper.resource)

    # Normalize reference values
    actual = normalize_reference_values(actual)
    expected_output = serialize_complex_types(test_helper.expected_output)
    expected_output = normalize_reference_values(expected_output)

    # Convert to DataFrames
    df_actual = pd.DataFrame(actual)
    df_expected = pd.DataFrame(expected_output)

    # Sort columns to ensure consistent comparison
    df_actual = df_actual[sorted(df_actual.columns)]
    df_expected = df_expected[sorted(df_expected.columns)]

    print("********* Actual")
    pprint(df_actual.to_dict(orient="records"))
    print("********* Expected")
    pprint(df_expected.to_dict(orient="records"))

    # Remove columns that we don't need
    for df in [df_actual, df_expected]:
        df.drop(
            columns=[
                "org_short_code",
                "registry_short_code",
                "hash_md5",
                "size_bytes",
                "last_processed",
                "status",
            ],
            inplace=True,
            errors="ignore",
        )

    # Remove id from subtype can't compare to uuid
    if resource_component:
        df_actual = df_actual.drop(columns=["id"])
        df_expected = df_expected.drop(columns=["id"])

    # Compare
    pd.testing.assert_frame_equal(df_actual, df_expected, check_dtype=False, check_exact=False)


def test_transformers_with_empty_rows():
    """
    Test Transformer Base class that filters out rows with empty data...
    Should return empty list
    """

    test_resource = {
        "resourceType": "Observation",
        "id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "extension": [
            {
                "valueIdentifier": {
                    "system": "",
                    "value": "",
                },
                "url": "",
            },
            {
                "valueIdentifier": {
                    "system": "",
                    "value": "",
                },
                "url": "",
            },
        ],
    }

    transformer = ObservationExtensionTransformer()
    out = transformer.transform_resource(0, test_resource)
    assert not out

    extensions = [
        {
            "valueIdentifier": {
                "system": "",
                "value": "",
            },
            "url": "",
        },
        {
            "valueIdentifier": {
                "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.707684",
                "value": "555",
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/template-id",
        },
    ]

    test_resource["extension"] = extensions
    out = transformer.transform_resource(0, test_resource)
    assert len(out) == 1


def test_raw_fhir_transformer():
    """
    Test cols function to verify correct columns and computed values are
    returned
    """

    transformer = RawFhirResourceTransformer()

    expected_cols = [
        "org_short_code",
        "registry_short_code",
        "hash_md5",
        "size_bytes",
        "last_processed",
        "status",
        "id",
        "resource_type",
        "json",
    ]

    column_metadata = transformer.column_metadata()
    assert len(expected_cols) == len(column_metadata)
    assert sorted(expected_cols) == sorted([meta.name for meta in column_metadata])

    patient = {"id": "p1", "resourceType": "Patient"}
    rows = transformer.transform_resources([patient])
    assert len(rows) == 1
    assert all(
        rows[0][c] == ""
        for c in [
            "org_short_code",
            "registry_short_code",
            "status",
        ]
    )
    # Verify last_processed has ISO 8601 format with timezone
    last_processed = rows[0]["last_processed"]
    try:
        dt = datetime.fromisoformat(last_processed)
        assert dt.tzinfo is not None, "Timestamp must have timezone info"
    except ValueError:
        pytest.fail(f"last_processed '{last_processed}' is not a valid ISO 8601 string")

    payload_str = json.dumps(patient, sort_keys=True, default=str, separators=(",", ":"))
    payload_bytes = payload_str.encode("utf-8")

    assert payload_str == rows[0]["json"]
    assert str(len(payload_bytes)) == rows[0]["size_bytes"]
    payload_hash = hashlib.md5(payload_bytes).hexdigest()
    assert rows[0]["hash_md5"] == payload_hash


def test_transformers_cols():
    """
    Test cols function to verify correct columns are returned
    """

    transformer = PatientAddressTransformer()

    expected_cols = [
        "id",
        "patient_id",
        "address_use",
        "address_type",
        "address_text",
        "address_line",
        "address_city",
        "address_district",
        "address_state",
        "address_postal_code",
        "address_country",
        "address_period_start",
        "address_period_end",
        "last_processed",
    ]

    column_metadata = transformer.column_metadata()
    assert len(expected_cols) == len(column_metadata)
    assert sorted(expected_cols) == sorted([meta.name for meta in column_metadata])
