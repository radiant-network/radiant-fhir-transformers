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

import pytest

from radiant_fhir_transform_cli.transform.classes import transformers
from tests.data import test_helpers


@pytest.mark.parametrize("test_helper_cls", list(test_helpers.values()))
def test_transformers(test_helper_cls):
    """
    Test every transformer class. Use test helper classes in tests.data
    """
    # Instantiate test helper class
    test_helper = test_helper_cls()

    # Instantiate transformer class based on resource type
    resource_type = test_helper_cls.resource_type
    cls = transformers.get(resource_type)
    transformer = cls()

    # Transform
    out = transformer.transform_resource(0, test_helper.resource)

    # Check output
    for k, v in out.items():
        assert test_helper.expected_output[k] == v
