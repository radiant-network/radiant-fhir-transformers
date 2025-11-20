"""FHIR Goal achievement_status_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_achievement_status_coding",
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
            "forEach": "achievementStatus.coding",
            "column": [
                {
                    "name": "achievement_status_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "achievement_status_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "achievement_status_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalAchievementStatusCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "achievement_status_coding", VIEW_DEFINITION)
