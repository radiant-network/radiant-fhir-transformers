"""
Test helper class for FHIR resource type Goal
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "example",
        "resource_type": "Goal",
        "lifecycle_status": "on-hold",
        "achievement_status_text": "Achieved",
        "priority_text": "high",
        "description_text": "Target weight is 160 to 180 lbs.",
        "subject_reference": "example",
        "subject_reference_type": None,
        "subject_display": "Peter James Chalmers",
        "start_date": "2015-04-05",
        "start_codeable_concept_text": None,
        "status_date": "2016-02-14",
        "status_reason": "Patient wants to defer weight loss until after honeymoon.",
        "expressed_by_reference": "example",
        "expressed_by_type": None,
        "expressed_by_display": "Peter James Chalmers",
    }
]


class GoalTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = GoalTransformer
    expected_table_name = "goal"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
