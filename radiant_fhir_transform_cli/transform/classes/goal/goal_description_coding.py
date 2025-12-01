"""FHIR Goal description_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_description_coding",
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
            "forEachOrNull": "description.coding",
            "column": [
                {
                    "name": "description_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "description_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "description_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalDescriptionCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "description_coding", VIEW_DEFINITION)
