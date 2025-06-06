"""
Test helper class for FHIR resource type CareTeam subtype ManagingOrganization
"""

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamManagingOrganizationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "care_team_id": "example",
        "managing_organization_reference": "f001",
        "managing_organization_type": None,
        "managing_organization_display": None,
    },
]


class CareTeamManagingOrganizationTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'CareTeam' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'CareTeam' resource.

    It predefines the resource type as 'CareTeam'
    and initializes the resource with the specific 'CareTeam' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'CareTeam'.
        resource (dict): The raw FHIR 'CareTeam' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'CareTeam' resource payload.
    """

    resource_type = "CareTeam"
    resource_subtype = "managing_organization"
    transformer = CareTeamManagingOrganizationTransformer
    expected_table_name = "care_team_managing_organization"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
