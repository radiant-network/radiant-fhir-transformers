"""FHIR Condition stage transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_stage",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "condition_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "stage",
            "column": [
                {
                    "name": "stage_summary_coding",
                    "path": "summary.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "stage_summary_text",
                    "path": "summary.text",
                    "type": "string",
                },
                {
                    "name": "stage_assessment",
                    "path": "assessment",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "stage_type_coding",
                    "path": "type.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "stage_type_text",
                    "path": "type.text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConditionStageTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Condition", "stage", VIEW_DEFINITION)
