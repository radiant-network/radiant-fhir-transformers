"""
FHIR Appointment Participant transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "appointment_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "participant",
        "columns": {
            # TODO: Add support for nested type fields
            "participant_type": {"fhir_key": "type", "type": "str"},
            "participant_actor_reference": {
                "fhir_key": "actor.reference",
                "type": "str",
            },
            "participant_actor_type": {
                "fhir_key": "actor.type",
                "type": "str",
            },
            "participant_actor_display": {
                "fhir_key": "actor.display",
                "type": "str",
            },
            "participant_required": {"fhir_key": "required", "type": "str"},
            "participant_status": {"fhir_key": "status", "type": "str"},
            "participant_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "participant_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class AppointmentParticipantTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'participant' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'participant' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('participant').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentParticipantTransformer instance with the resource type 'Appointment',
            subtype 'participant', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", "participant", TRANSFORM_SCHEMA)
