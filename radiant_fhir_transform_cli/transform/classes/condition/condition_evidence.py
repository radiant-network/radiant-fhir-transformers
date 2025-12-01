"""FHIR Condition evidence transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_evidence",
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
            "forEach": "evidence",
            "column": [
                {
                    "name": "evidence_code",
                    "path": "code",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "evidence_detail",
                    "path": "detail",
                    "type": "string",
                    "collection": True,
                },
            ],
        },
    ],
}


class ConditionEvidenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Condition", "evidence", VIEW_DEFINITION)
