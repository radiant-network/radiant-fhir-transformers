"""FHIR Condition severity_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_severity_coding",
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
                    "name": "condition_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "severity.coding",
            "column": [
                {
                    "name": "severity_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "severity_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "severity_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConditionSeverityCodingTransformer(FhirResourceTransformer):
    resource_type = "Condition"
    resource_component = "severity_coding"
    view_definition = VIEW_DEFINITION
