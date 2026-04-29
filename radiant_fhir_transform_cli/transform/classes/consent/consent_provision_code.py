"""FHIR Consent provision_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_code",
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
            "forEachOrNull": "provision.code",
            "column": [
                {
                    "name": "provision_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "provision_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentProvisionCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_code", VIEW_DEFINITION)
