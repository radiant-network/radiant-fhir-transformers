"""FHIR Appointment specialty transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_specialty",
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
            "forEach": "specialty",
            "column": [
                {
                    "name": "specialty_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "specialty_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "specialty_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "specialty_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class AppointmentSpecialtyTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "specialty", VIEW_DEFINITION)
