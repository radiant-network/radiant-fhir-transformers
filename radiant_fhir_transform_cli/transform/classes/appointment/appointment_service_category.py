"""FHIR Appointment service_category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_service_category",
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
            "forEachOrNull": "serviceCategory",
            "column": [
                {
                    "name": "service_category_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "service_category_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "service_category_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "service_category_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class AppointmentServiceCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "service_category", VIEW_DEFINITION)
