"""
Test helper class for FHIR resource type CareTeam subtype ReasonCode
"""

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_code_coding": {
            "system": "http://snomed.info/sct",
            "code": "400097005",
            "display": "Ingrowing nail",
        },
        "reason_code_text": "Ingrowing nail",
        "id": "8af0ab58-3f31-4b44-a030-1268aa04dfe8",
        "care_team_id": "example",
    },
]


class CareTeamReasonCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_code"
    transformer = CareTeamReasonCodeTransformer
    expected_table_name = "care_team_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
