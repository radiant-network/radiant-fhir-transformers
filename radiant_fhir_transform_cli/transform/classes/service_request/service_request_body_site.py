"""FHIR ServiceRequest body_site transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_body_site",
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
            "forEachOrNull": "bodySite",
            "column": [
                {
                    "name": "body_site_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "body_site_coding",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ServiceRequestBodySiteTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "body_site", VIEW_DEFINITION)
