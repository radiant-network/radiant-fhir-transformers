"""
Test helper class for FHIR resource type Condition subtype Identifier 
"""

from radiant_fhir_transform_cli.transform.classes.condition.condition_identifier import (
    ConditionIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "condition_id": "f201",
        "identifier_value": "12345",
        "identifier_use": None,
        "identifier_system": None,
    },
]


class ConditionIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Condition' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Condition' resource.

    It predefines the resource type as 'Condition'
    and initializes the resource with the specific 'Condition' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Condition'.

        resource (dict): The raw FHIR 'Condition' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Condition' resource payload.
    """

    resource_type = "Condition"
    resource_subtype = "identifier"
    transformer = ConditionIdentifierTransformer
    expected_table_name = "condition_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
