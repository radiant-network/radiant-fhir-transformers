"""
Test helper class for FHIR resource type CareTeam subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": None,
        "identifier_value": "12345",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "c55d9737-0d5c-4f78-bf4f-f334d625624e",
        "care_team_id": "example",
    },
]


class CareTeamIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = CareTeamIdentifierTransformer
    expected_table_name = "care_team_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
