"""FHIR Goal start_codeable_concept_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_start_codeable_concept_coding",
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
            "forEachOrNull": "startCodeableConcept.coding",
            "column": [
                {
                    "name": "start_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "start_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "start_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalStartCodeableConceptCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Goal", "start_codeable_concept_coding", VIEW_DEFINITION
        )
