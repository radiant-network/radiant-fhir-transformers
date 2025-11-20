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
                    "name": "consent_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "provision.action",
            "column": [
                {
                    "name": "provision_action_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "provision_action_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "provision_action_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ConsentProvisionActionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_action", VIEW_DEFINITION)
