"""FHIR Goal outcome_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_outcome_reference",
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
            "forEachOrNull": "outcomeReference",
            "column": [
                {
                    "name": "outcome_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "outcome_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "outcome_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalOutcomeReferenceTransformer(FhirResourceTransformer):
    resource_type = "Goal"
    resource_component = "outcome_reference"
    view_definition = VIEW_DEFINITION
