"""FHIR Consent provision_security_label transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_security_label",
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
            "forEach": "provision.securityLabel",
            "column": [
                {
                    "name": "provision_security_label_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "provision_security_label_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "provision_security_label_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentProvisionSecurityLabelTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_security_label", VIEW_DEFINITION)
