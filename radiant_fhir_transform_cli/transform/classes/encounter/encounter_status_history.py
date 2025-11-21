"""FHIR Encounter status_history transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_status_history",
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
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "statusHistory",
            "column": [
                {
                    "name": "status_history_status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "status_history_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "status_history_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class EncounterStatusHistoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "status_history", VIEW_DEFINITION)
