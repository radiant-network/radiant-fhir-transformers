"""FHIR ServiceRequest replaces transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_replaces",
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
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "replaces",
            "column": [
                {
                    "name": "replaces_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "replaces_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "replaces_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestReplacesTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "replaces", VIEW_DEFINITION)
