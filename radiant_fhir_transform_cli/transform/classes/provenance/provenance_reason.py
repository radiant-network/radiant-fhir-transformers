"""FHIR Provenance reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_reason",
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
                    "name": "provenance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "reason",
            "column": [
                {
                    "name": "reason_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "reason_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "reason_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "reason_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProvenanceReasonTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", "reason", VIEW_DEFINITION)
