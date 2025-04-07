"""
Test transformer classes with test helpers in tests.data
"""
import pytest

from radiant_fhir_transform_cli.transform.classes import transformers
from tests.data import test_helpers


@pytest.mark.parametrize(
    "test_helper_cls",
    list(test_helpers.values())
)
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
