"""FHIR Goal priority_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_priority_coding",
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
                    "name": "goal_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "priority.coding",
            "column": [
                {
                    "name": "priority_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "priority_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "priority_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalPriorityCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "priority_coding", VIEW_DEFINITION)
