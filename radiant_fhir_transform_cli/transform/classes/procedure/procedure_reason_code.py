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
            "forEachOrNull": "reasonCode",
            "column": [
                {
                    "name": "reason_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "reason_code_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "reason_code_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "reason_code_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProcedureReasonCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "reason_code", VIEW_DEFINITION)
