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
            "forEachOrNull": "provision.securityLabel",
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
    resource_type = "Consent"
    resource_component = "provision_security_label"
    view_definition = VIEW_DEFINITION
