"""
Test helper class for FHIR resource type CarePlan subtype CareTeam
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanCareTeamTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "care_plan_id": "preg",
        "care_team_reference": "#careteam",
        "care_team_display": None,
        "care_team_type": None,
    },
]


class CarePlanCareTeamTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'CarePlan' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'CarePlan' resource.

    It predefines the resource type as 'CarePlan'
    and initializes the resource with the specific 'CarePlan' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'CarePlan'.

        resource (dict): The raw FHIR 'CarePlan' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'CarePlan' resource payload.
    """

    resource_type = "CarePlan"
    resource_subtype = "care_team"
    transformer = CarePlanCareTeamTransformer
    expected_table_name = "care_plan_care_team"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
