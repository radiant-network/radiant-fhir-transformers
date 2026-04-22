"""FHIR Consent organization transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_organization",
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
            "forEachOrNull": "organization",
            "column": [
                {
                    "name": "organization_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "organization_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "organization_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentOrganizationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "organization", VIEW_DEFINITION)
