"""FHIR AllergyIntolerance category transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "AllergyIntolerance",
    "name": "allergy_intolerance_category",
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
                    "name": "allergy_intolerance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "category",
            "column": [
                {
                    "name": "category",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class AllergyIntoleranceCategoryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("AllergyIntolerance", "category", VIEW_DEFINITION)
