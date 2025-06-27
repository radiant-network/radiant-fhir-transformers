"""
FHIR Appointment transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": "id",
        "columns": {"id": {"fhir_key": "id", "type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {
                "fhir_key": "resourceType",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "cancelationReason.text",
        "columns": {
            "cancelation_reason_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "appointmentType.text",
        "columns": {
            "appointment_type_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "priority",
        "columns": {"priority": {"fhir_key": "priority", "type": "int"}},
    },
    {
        "fhir_path": "description",
        "columns": {"description": {"fhir_key": "description", "type": "str"}},
    },
    {
        "fhir_path": "start",
        "columns": {"start": {"fhir_key": "start", "type": "datetime"}},
    },
    {
        "fhir_path": "end",
        "columns": {"end": {"fhir_key": "end", "type": "datetime"}},
    },
    {
        "fhir_path": "minutesDuration",
        "columns": {
            "minutes_duration": {"fhir_key": "minutesDuration", "type": "int"}
        },
    },
    {
        "fhir_path": "created",
        "columns": {"created": {"fhir_key": "created", "type": "datetime"}},
    },
    {
        "fhir_path": "comment",
        "columns": {"comment": {"fhir_key": "comment", "type": "str"}},
    },
    {
        "fhir_path": "patientInstruction",
        "columns": {
            "patient_instruction": {
                "fhir_key": "patientInstruction",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "Appointment",
        "columns": {
            "appointment_raw_json": {
                "type": "str",
            }
        },
    },
]


class AppointmentTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR.

    Transform Appointment JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the AppointmentTransformer instance with the resource
            type 'Appointment' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", None, TRANSFORM_SCHEMA)
