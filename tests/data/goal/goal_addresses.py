"""
Test helper class for FHIR resource type Goal subtype Addresses
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalAddressesTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "goal_id": "example",
        "addresses_reference": None,
        "addresses_type": None,
        "addresses_display": "obesity condition",
    },
]


class GoalAddressesTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "addresses"
    transformer = GoalAddressesTransformer
    expected_table_name = "goal_addresses"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
