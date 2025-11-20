"""FHIR Procedure complication transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_complication",
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
            "forEach": "complication",
            "column": [
                {
                    "name": "complication_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "complication_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "complication_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "complication_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProcedureComplicationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "complication", VIEW_DEFINITION)
