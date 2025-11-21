"""
Test helper class for FHIR resource type Condition subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.condition.condition_code_coding import (
    ConditionCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://snomed.info/sct",
        "code_coding_code": "386661006",
        "code_coding_display": "Fever",
        "id": "74730882-a3c8-4d44-a27a-bfc0508184b6",
        "condition_id": "f201",
    },
]


class ConditionCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = ConditionCodeCodingTransformer
    expected_table_name = "condition_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
