"""
Test helper class for FHIR resource type Condition subtype Category
"""

from radiant_fhir_transform_cli.transform.classes.condition.condition_category import (
    ConditionCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "category_coding_system": "http://snomed.info/sct",
        "category_coding_code": "55607006",
        "category_coding_display": "Problem",
        "category_text": None,
        "id": "bef767f6-519d-4fc5-b6d2-a89dd2ae1521",
        "condition_id": "f201",
    },
    {
        "category_coding_system": "http://terminology.hl7.org/CodeSystem/condition-category",
        "category_coding_code": "problem-list-item",
        "category_coding_display": None,
        "category_text": None,
        "id": "223b0c21-553c-4566-b9ec-ac348125df06",
        "condition_id": "f201",
    },
]


class ConditionCategoryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category"
    transformer = ConditionCategoryTransformer
    expected_table_name = "condition_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
