"""FHIR Procedure reason_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_reason_code",
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
            "forEachOrNull": "reasonCode",
            "column": [
                {
                    "name": "reason_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "reason_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureReasonCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "reason_code", VIEW_DEFINITION)
