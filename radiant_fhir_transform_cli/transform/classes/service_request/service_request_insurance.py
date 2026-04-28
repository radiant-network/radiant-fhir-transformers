"""FHIR ServiceRequest insurance transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_insurance",
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
            "forEachOrNull": "insurance",
            "column": [
                {
                    "name": "insurance_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "insurance_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "insurance_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestInsuranceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "insurance", VIEW_DEFINITION)
