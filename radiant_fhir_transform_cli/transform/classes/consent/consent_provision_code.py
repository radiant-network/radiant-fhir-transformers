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
            "forEachOrNull": "provision.code",
            "column": [
                {
                    "name": "provision_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "provision_code_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "provision_code_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "provision_code_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ConsentProvisionCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_code", VIEW_DEFINITION)
