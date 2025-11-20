"""FHIR CarePlan category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_category",
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
                    "name": "care_plan_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "category",
            "column": [
                {
                    "name": "category_coding",
                    "path": "coding",
                    "type": "string",
                },
                {
                    "name": "category_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "category", VIEW_DEFINITION)
