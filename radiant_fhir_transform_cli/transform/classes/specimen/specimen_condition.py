"""FHIR Specimen condition transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_condition",
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
                    "name": "specimen_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "condition",
            "column": [
                {
                    "name": "condition_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "condition_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "condition_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "condition_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class SpecimenConditionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "condition", VIEW_DEFINITION)
