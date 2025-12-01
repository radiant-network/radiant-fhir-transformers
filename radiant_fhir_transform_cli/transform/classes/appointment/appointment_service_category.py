"""FHIR Appointment service_category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_service_category",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "appointment_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "serviceCategory",
            "column": [
                {
                    "name": "service_category_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "service_category_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentServiceCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "service_category", VIEW_DEFINITION)
