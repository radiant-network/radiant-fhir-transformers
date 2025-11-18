"""FHIR Condition severity_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_severity_coding",
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
            "forEach": "severity.coding",
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
    def __init__(self):
        super().__init__("Condition", "severity_coding", VIEW_DEFINITION)
