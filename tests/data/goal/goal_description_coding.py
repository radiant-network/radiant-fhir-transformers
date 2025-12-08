"""
Test helper class for FHIR resource type Goal subtype Description Coding
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalDescriptionCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "description_coding_system": "http://snomed.info/sct",
        "description_coding_code": "243862009",
        "description_coding_display": "Obesity monitoring status (finding)",
        "id": "32c04cab-6697-466c-945b-d7c1e7ac8c3f",
        "goal_id": "example",
    },
]


class GoalDescriptionCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "description_coding"
    transformer = GoalDescriptionCodingTransformer
    expected_table_name = "goal_description_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
