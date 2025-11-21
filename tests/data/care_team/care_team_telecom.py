"""
Test helper class for FHIR resource type CareTeam subtype Telecom
"""

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamTelecomTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "telecom_system": "phone",
        "telecom_value": "215-590-3326",
        "telecom_use": "work",
        "telecom_rank": None,
        "telecom_period_start": None,
        "telecom_period_end": None,
        "id": "080c7ec1-7cb5-4a34-bbce-880a60255bcb",
        "care_team_id": "example",
    },
    {
        "telecom_system": "fax",
        "telecom_value": "215-590-3606",
        "telecom_use": "work",
        "telecom_rank": None,
        "telecom_period_start": None,
        "telecom_period_end": None,
        "id": "1081eb9c-5e5e-4028-b42f-e9de74d2630d",
        "care_team_id": "example",
    },
]


class CareTeamTelecomTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "telecom"
    transformer = CareTeamTelecomTransformer
    expected_table_name = "care_team_telecom"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
