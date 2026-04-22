"""FHIR Consent performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_performer",
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
                    "name": "consent_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "performer",
            "column": [
                {
                    "name": "performer_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "performer_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "performer_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentPerformerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "performer", VIEW_DEFINITION)
