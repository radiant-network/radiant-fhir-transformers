"""FHIR ServiceRequest supporting_info transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_supporting_info",
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
            "forEachOrNull": "supportingInfo",
            "column": [
                {
                    "name": "supporting_info_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "supporting_info_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "supporting_info_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestSupportingInfoTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "supporting_info", VIEW_DEFINITION)
