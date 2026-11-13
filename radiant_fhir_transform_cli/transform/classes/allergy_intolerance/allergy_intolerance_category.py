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
                    "name": "allergy_intolerance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "category",
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
    resource_type = "AllergyIntolerance"
    resource_component = "category"
    view_definition = VIEW_DEFINITION
