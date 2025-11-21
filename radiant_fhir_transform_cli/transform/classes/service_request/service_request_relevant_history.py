"""FHIR ServiceRequest relevant_history transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_relevant_history",
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
            "forEachOrNull": "relevantHistory",
            "column": [
                {
                    "name": "relevant_history_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "relevant_history_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "relevant_history_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestRelevantHistoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "relevant_history", VIEW_DEFINITION)
