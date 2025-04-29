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

import pandas as pd
import pytest

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationExtensionTransformer,
)
from tests.data import test_helpers


@pytest.mark.parametrize("test_helper_cls", list(test_helpers))
def test_transformers(test_helper_cls):
    """
    Test every transformer class. Use test helper classes in tests.data
    """
    # Instantiate test helper class
    test_helper = test_helper_cls()

    # Instantiate transformer class based on resource type
    resource_type = test_helper_cls.resource_type
    resource_subtype = test_helper.resource_subtype

    cls = test_helper_cls.transformer

    transformer = cls()

    assert test_helper.expected_table_name == transformer.table_name

    # Transform
    outs = transformer.transform_resource(0, test_helper.resource)
    # Convert to DataFrames
    df_actual = pd.DataFrame(outs)
    df_expected = pd.DataFrame(test_helper.expected_output)

    # Sort columns to ensure consistent comparison
    df_actual = df_actual[sorted(df_actual.columns)]
    df_expected = df_expected[sorted(df_expected.columns)]

    # Remove id from subtype can't compare to uuid
    if resource_subtype:
        df_actual = df_actual.drop(columns=["id"])

    # Compare
    pd.testing.assert_frame_equal(
        df_actual, df_expected, check_dtype=False, check_exact=False
    )


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
