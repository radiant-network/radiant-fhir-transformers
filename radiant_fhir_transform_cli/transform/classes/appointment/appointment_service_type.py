"""FHIR Appointment service_type transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_service_type",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
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
            "forEachOrNull": "serviceType",
            "column": [
                {
                    "name": "service_type_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "service_type_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentServiceTypeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "service_type", VIEW_DEFINITION)
