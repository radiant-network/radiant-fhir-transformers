"""
Test helper class for FHIR resource type Goal subtype Priority Coding
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalPriorityCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "priority_coding_system": "http://terminology.hl7.org/CodeSystem/goal-priority",
        "priority_coding_code": "high-priority",
        "priority_coding_display": "High Priority",
        "id": "802b7dca-7ec4-40d0-bff7-844cd78c2eb5",
        "goal_id": "example",
    },
]


class GoalPriorityCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "priority_coding"
    transformer = GoalPriorityCodingTransformer
    expected_table_name = "goal_priority_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
