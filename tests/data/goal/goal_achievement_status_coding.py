"""
Test helper class for FHIR resource type Goal subtype AchievementStatus Coding
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalAchievementStatusCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "achievement_status_coding_system": "http://terminology.hl7.org/CodeSystem/goal-achievement",
        "achievement_status_coding_code": "achieved",
        "achievement_status_coding_display": "Achieved",
        "id": "99296dab-3476-48e0-8fb5-d78acf58e39a",
        "goal_id": "example",
    },
]


class GoalAchievementStatusCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "achievement_status_coding"
    transformer = GoalAchievementStatusCodingTransformer
    expected_table_name = "goal_achievement_status_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
