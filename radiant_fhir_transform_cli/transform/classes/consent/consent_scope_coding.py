"""FHIR Consent scope_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_scope_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "consent_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "scope.coding",
            "column": [
                {
                    "name": "scope_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {"name": "scope_coding_code", "path": "code", "type": "string"},
                {
                    "name": "scope_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentScopeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "scope_coding", VIEW_DEFINITION)
