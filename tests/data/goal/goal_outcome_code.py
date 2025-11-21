"""
Test helper class for FHIR resource type Goal subtype OutcomeCode
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalOutcomeCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "outcome_code_coding_system": "http://snomed.info/sct",
        "outcome_code_coding_code": "262285001",
        "outcome_code_coding_display": "Weight decreased (finding)",
        "outcome_code_text": None,
        "id": "11d90d26-1670-48c7-aa14-35c7cc832424",
        "goal_id": "example",
    },
]


class GoalOutcomeCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "outcome_code"
    transformer = GoalOutcomeCodeTransformer
    expected_table_name = "goal_outcome_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
