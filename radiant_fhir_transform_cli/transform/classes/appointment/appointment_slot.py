"""FHIR Appointment slot transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_slot",
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
            "forEachOrNull": "slot",
            "column": [
                {
                    "name": "slot_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "slot_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "slot_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentSlotTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "slot", VIEW_DEFINITION)
