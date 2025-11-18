"""FHIR Condition category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_category",
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
            "forEach": "category",
            "column": [
                {
                    "name": "category_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "category_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class ConditionCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Condition", "category", VIEW_DEFINITION)
