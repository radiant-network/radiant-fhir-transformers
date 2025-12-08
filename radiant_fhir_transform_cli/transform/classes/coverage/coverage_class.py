"""FHIR Coverage class transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_class",
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
                    "name": "coverage_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "class",
            "column": [
                {
                    "name": "class_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "class_value",
                    "path": "value",
                    "type": "string",
                },
                {
                    "name": "class_name",
                    "path": "name",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "type.coding",
                    "column": [
                        {
                            "name": "class_type_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "class_type_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class CoverageClassTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Coverage", "class", VIEW_DEFINITION)
