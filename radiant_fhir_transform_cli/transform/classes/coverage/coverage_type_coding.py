"""FHIR Coverage type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_type_coding",
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
                    "name": "coverage_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "type.coding",
            "column": [
                {
                    "name": "type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class CoverageTypeCodingTransformer(FhirResourceTransformer):
    resource_type = "Coverage"
    resource_component = "type_coding"
    view_definition = VIEW_DEFINITION
