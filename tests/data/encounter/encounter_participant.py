"""
Test helper class for FHIR resource type Encounter subtype Participant
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_participant import (
    EncounterParticipantTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE
EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "participant_type": [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                            "code": "PART",
                        }
                    ]
                }
            ],
        "participant_period": None,
        "participant_individual": {"reference": "Practitioner/f201"},
    }
]

class EncounterParticipantTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'participant'.

        transformer (class): The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the table where the transformed data is expected to be stored.
    """

    resource_type = "Encounter"
    resource_subtype = "participant"
    transformer = EncounterParticipantTransformer
    expected_table_name = "encounter_participant"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)