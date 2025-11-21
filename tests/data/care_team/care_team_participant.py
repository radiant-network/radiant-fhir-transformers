"""
Test helper class for FHIR resource type CareTeam subtype Participant
"""

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamParticipantTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "participant_role_text": "responsiblePerson",
        "participant_role_coding_system": None,
        "participant_role_coding_code": None,
        "participant_role_coding_display": None,
        "participant_member_reference": "Patient/example",
        "participant_member_type": None,
        "participant_member_display": "Peter James Chalmers",
        "participant_on_behalf_of_reference": None,
        "participant_on_behalf_of_type": None,
        "participant_on_behalf_of_display": None,
        "participant_period_start": None,
        "participant_period_end": None,
        "id": "81c257b3-8bd3-4964-acee-a37109acd890",
        "care_team_id": "example",
    },
    {
        "participant_role_text": "adviser",
        "participant_role_coding_system": None,
        "participant_role_coding_code": None,
        "participant_role_coding_display": None,
        "participant_member_reference": "Practitioner/pr1",
        "participant_member_type": None,
        "participant_member_display": "Dorothy Dietition",
        "participant_on_behalf_of_reference": "Organization/f001",
        "participant_on_behalf_of_type": None,
        "participant_on_behalf_of_display": None,
        "participant_period_start": None,
        "participant_period_end": "2013-01-01",
        "id": "d49930c5-b6e1-41de-ae61-306235a1a12e",
        "care_team_id": "example",
    },
]


class CareTeamParticipantTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "participant"
    transformer = CareTeamParticipantTransformer
    expected_table_name = "care_team_participant"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
