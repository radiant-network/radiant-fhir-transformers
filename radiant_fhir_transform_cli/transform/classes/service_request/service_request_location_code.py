"""FHIR ServiceRequest location_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_location_code",
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
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "locationCode",
            "column": [
                {
                    "name": "location_code_coding",
                    "path": "coding",
                    "type": "string",
                },
                {
                    "name": "location_code_text",
                    "path": "text",
                    "type": "string",
                },
                {
                    "name": "location_code_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestLocationCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "location_code", VIEW_DEFINITION)
