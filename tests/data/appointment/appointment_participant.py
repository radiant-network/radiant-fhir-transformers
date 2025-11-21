"""
Test helper class for FHIR resource type Appointment subtype Participant 
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_participant import (
    AppointmentParticipantTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "participant_type": None,
        "participant_actor_reference": "Patient/example",
        "participant_actor_type": None,
        "participant_actor_display": "Peter James Chalmers",
        "participant_required": "required",
        "participant_status": "accepted",
        "participant_period_start": None,
        "participant_period_end": None,
        "id": "60f7336c-3dfd-4029-a627-553bde1cceac",
        "appointment_id": "example",
    },
    {
        "participant_type": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                    "code": "ATND",
                },
            ],
        },
        "participant_actor_reference": "Practitioner/example",
        "participant_actor_type": None,
        "participant_actor_display": "Dr Adam Careful",
        "participant_required": "required",
        "participant_status": "accepted",
        "participant_period_start": None,
        "participant_period_end": None,
        "id": "85ae196d-4eb6-4af8-8215-f6e891c83118",
        "appointment_id": "example",
    },
    {
        "participant_type": None,
        "participant_actor_reference": "Location/1",
        "participant_actor_type": None,
        "participant_actor_display": "South Wing, second floor",
        "participant_required": "required",
        "participant_status": "accepted",
        "participant_period_start": None,
        "participant_period_end": None,
        "id": "9b3d0fdb-f0de-4d43-a0ab-2218d2f11f2b",
        "appointment_id": "example",
    },
]


class AppointmentParticipantTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Appointment' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Appointment' resource.

    It predefines the resource type as 'Appointment'
    and initializes the resource with the specific 'Appointment' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Appointment'.

        resource (dict): The raw FHIR 'Appointment' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Appointment' resource payload.
    """

    resource_type = "Appointment"
    resource_subtype = "participant"
    transformer = AppointmentParticipantTransformer
    expected_table_name = "appointment_participant"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
