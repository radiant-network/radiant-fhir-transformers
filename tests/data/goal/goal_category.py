"""
Test helper class for FHIR resource type Goal subtype Category
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "goal_id": "example",
        "category_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/goal-category",
                "code": "dietary",
            }
        ],
        "category_text": None,
    },
]


class GoalCategoryTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Goal' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Goal' resource.

    It predefines the resource type as 'Goal'
    and initializes the resource with the specific 'Goal' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Goal'.
        resource (dict): The raw FHIR 'Goal' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Goal' resource payload.
    """

    resource_type = "Goal"
    resource_subtype = "category"
    transformer = GoalCategoryTransformer
    expected_table_name = "goal_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
