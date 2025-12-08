"""FHIR Appointment reason_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_reason_reference",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "appointment_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "reasonReference",
            "column": [
                {
                    "name": "reason_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "reason_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "reason_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentReasonReferenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "reason_reference", VIEW_DEFINITION)
