"""FHIR Consent provision_action transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_action",
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
            "forEachOrNull": "provision.action",
            "column": [
                {
                    "name": "provision_action_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "provision_action_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentProvisionActionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_action", VIEW_DEFINITION)
