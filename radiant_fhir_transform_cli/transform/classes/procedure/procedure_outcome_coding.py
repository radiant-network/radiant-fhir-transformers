"""FHIR Procedure outcome_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_outcome_coding",
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
                    "name": "procedure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "outcome.coding",
            "column": [
                {
                    "name": "outcome_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "outcome_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "outcome_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureOutcomeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "outcome_coding", VIEW_DEFINITION)
