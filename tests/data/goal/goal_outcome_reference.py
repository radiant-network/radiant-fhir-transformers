"""
Test helper class for FHIR resource type Goal subtype OutcomeReference
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalOutcomeReferenceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "outcome_reference_reference": "Observation/example",
        "outcome_reference_type": None,
        "outcome_reference_display": "Body Weight Measured",
        "id": "d8a41a5e-ef31-4b99-aa51-1dc5bb154492",
        "goal_id": "example",
    },
]


class GoalOutcomeReferenceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "outcome_reference"
    transformer = GoalOutcomeReferenceTransformer
    expected_table_name = "goal_outcome_reference"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
