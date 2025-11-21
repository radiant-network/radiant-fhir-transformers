"""FHIR Goal outcome_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_outcome_code",
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
            "forEachOrNull": "outcomeCode",
            "column": [
                {
                    "name": "outcome_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "outcome_code_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "outcome_code_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "outcome_code_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class GoalOutcomeCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "outcome_code", VIEW_DEFINITION)
