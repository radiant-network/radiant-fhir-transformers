"""FHIR MedicationRequest event_history transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_event_history",
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
                    "name": "medication_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "eventHistory",
            "column": [
                {
                    "name": "event_history_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "event_history_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "event_history_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationRequestEventHistoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationRequest", "event_history", VIEW_DEFINITION)
