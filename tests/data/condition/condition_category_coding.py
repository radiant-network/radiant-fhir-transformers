"""
Test helper class for FHIR resource type Condition subtype Category Coding
"""

from radiant_fhir_transform_cli.transform.classes.condition.condition_category_coding import (
    ConditionCategoryCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "condition_id": "f201",
        "category_coding_system":  "http://snomed.info/sct",
        "category_coding_code": "55607006",
        "category_coding_display": "Problem",
    },
    {
        "condition_id": "f201",
        "category_coding_system": "http://terminology.hl7.org/CodeSystem/condition-category",
        "category_coding_code": "problem-list-item",
        "category_coding_display": None,
    }
]


class ConditionCategoryCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category_coding"
    transformer = ConditionCategoryCodingTransformer
    expected_table_name = "condition_category_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
