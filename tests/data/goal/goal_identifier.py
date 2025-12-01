"""
Test helper class for FHIR resource type Goal subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": None,
        "identifier_value": "123",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "d9dbe80b-fd5b-46f4-a5b6-8592c753f41b",
        "goal_id": "example",
    },
]


class GoalIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = GoalIdentifierTransformer
    expected_table_name = "goal_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
