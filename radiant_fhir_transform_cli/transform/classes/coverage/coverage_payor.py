"""FHIR Coverage payor transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_payor",
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
            "forEachOrNull": "payor",
            "column": [
                {
                    "name": "payor_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "payor_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "payor_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class CoveragePayorTransformer(FhirResourceTransformer):
    resource_type = "Coverage"
    resource_component = "payor"
    view_definition = VIEW_DEFINITION
