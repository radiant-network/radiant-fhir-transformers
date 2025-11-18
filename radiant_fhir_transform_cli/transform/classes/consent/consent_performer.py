"""FHIR Consent performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_performer",
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
            "forEach": "performer",
            "column": [
                {
                    "name": "performer_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "performer_type", "path": "type", "type": "string"},
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
