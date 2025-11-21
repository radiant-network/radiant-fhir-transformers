"""
Test helper class for FHIR resource type CareTeam subtype Note
"""

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "note_author_reference_reference": None,
        "note_author_reference_type": None,
        "note_author_reference_display": None,
        "note_author_string": None,
        "note_time": None,
        "note_text": "Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding.",
        "id": "674a407c-7965-461c-b913-d177a720ad63",
        "care_team_id": "example",
    },
]


class CareTeamNoteTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "note"
    transformer = CareTeamNoteTransformer
    expected_table_name = "care_team_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
