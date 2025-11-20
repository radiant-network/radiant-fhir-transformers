"""FHIR Appointment transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "cancelation_reason_text",
                    "path": "cancelationReason.text",
                    "type": "string",
                },
                {
                    "name": "appointment_type_text",
                    "path": "appointmentType.text",
                    "type": "string",
                },
                {
                    "name": "priority",
                    "path": "priority",
                    "type": "integer",
                },
                {
                    "name": "description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "start",
                    "path": "start",
                    "type": "dateTime",
                },
                {
                    "name": "end",
                    "path": "end",
                    "type": "dateTime",
                },
                {
                    "name": "minutes_duration",
                    "path": "minutesDuration",
                    "type": "integer",
                },
                {
                    "name": "created",
                    "path": "created",
                    "type": "dateTime",
                },
                {
                    "name": "comment",
                    "path": "comment",
                    "type": "string",
                },
                {
                    "name": "patient_instruction",
                    "path": "patientInstruction",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", None, VIEW_DEFINITION)
