"""
Test helper class for FHIR resource type CareTeam
"""

import json

from radiant_fhir_transform_cli.transform.classes.care_team import (
    CareTeamTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_team_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "example",
        "resource_type": "CareTeam",
        "status": "active",
        "name": "Peter James Charlmers Care Plan for Inpatient Encounter",
        "subject_reference": "example",
        "subject_type": None,
        "subject_display": "Peter James Chalmers",
        "encounter_reference": "example",
        "encounter_type": None,
        "encounter_display": None,
        "period_start": None,
        "period_end": "2013-01-01",
        "care_team_raw_json": json.dumps(RESOURCE),
    }
]


class CareTeamTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = CareTeamTransformer
    expected_table_name = "care_team"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
