"""FHIR ServiceRequest reason_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_reason_code",
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
            "forEach": "reasonCode",
            "column": [
                {
                    "name": "reason_code_coding",
                    "path": "coding",
                    "collection": True,
                },
                {
                    "name": "reason_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestReasonCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "reason_code", VIEW_DEFINITION)
