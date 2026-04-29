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
                    "name": "outcome_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "outcome_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalOutcomeCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "outcome_code", VIEW_DEFINITION)
