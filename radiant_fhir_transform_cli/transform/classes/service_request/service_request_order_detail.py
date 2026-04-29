"""FHIR ServiceRequest order_detail transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_order_detail",
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
            "forEachOrNull": "orderDetail",
            "column": [
                {
                    "name": "order_detail_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "order_detail_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestOrderDetailTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "order_detail", VIEW_DEFINITION)
