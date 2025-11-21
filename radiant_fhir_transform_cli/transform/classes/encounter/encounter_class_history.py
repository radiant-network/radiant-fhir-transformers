"""FHIR Encounter class_history transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_class_history",
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
            "forEachOrNull": "classHistory",
            "column": [
                {
                    "name": "class_history_class_system",
                    "path": "class.system",
                    "type": "string",
                },
                {
                    "name": "class_history_class_code",
                    "path": "class.code",
                    "type": "string",
                },
                {
                    "name": "class_history_class_display",
                    "path": "class.display",
                    "type": "string",
                },
                {
                    "name": "class_history_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "class_history_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class EncounterClassHistoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "class_history", VIEW_DEFINITION)
