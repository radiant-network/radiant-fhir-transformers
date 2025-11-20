"""FHIR Procedure code_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_code_coding",
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
            "forEach": "code.coding",
            "column": [
                {
                    "name": "code_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "code_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "code_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProcedureCodeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "code_coding", VIEW_DEFINITION)
