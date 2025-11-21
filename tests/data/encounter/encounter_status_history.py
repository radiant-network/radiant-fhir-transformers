"""
Test helper class for FHIR resource type Encounter subtype StatusHistory
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterStatusHistoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "status_history_status": "arrived",
        "status_history_period_start": "2013-03-08",
        "status_history_period_end": None,
        "id": "d101e3b2-fa22-48be-a375-6548d1eef9a5",
        "encounter_id": "f203",
    },
]


class EncounterStatusHistoryTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource.

    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.

        resource (dict): The raw FHIR 'Encounter' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Encounter' resource payload.
    """

    resource_type = "Encounter"
    resource_subtype = "status_history"
    transformer = EncounterStatusHistoryTransformer
    expected_table_name = "encounter_status_history"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
