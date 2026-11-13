"""FHIR Procedure category_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_category_coding",
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
                    "name": "procedure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "category.coding",
            "column": [
                {
                    "name": "category_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "category_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "category_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureCategoryCodingTransformer(FhirResourceTransformer):
    resource_type = "Procedure"
    resource_component = "category_coding"
    view_definition = VIEW_DEFINITION
