"""FHIR Condition evidence transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_evidence",
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
                    "name": "condition_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "evidence",
            "column": [],
            "select": [
                {
                    "forEach": "code",
                    "column": [
                        {
                            "name": "evidence_code_coding",
                            "path": "coding",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEach": "detail",
                    "column": [
                        {
                            "name": "evidence_detail_reference",
                            "path": "reference",
                            "type": "string",
                        },
                        {
                            "name": "evidence_detail_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ConditionEvidenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Condition", "evidence", VIEW_DEFINITION)
