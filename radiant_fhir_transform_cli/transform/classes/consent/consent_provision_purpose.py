"""FHIR Consent provision_purpose transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_purpose",
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
            "forEachOrNull": "provision.purpose",
            "column": [
                {
                    "name": "provision_purpose_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "provision_purpose_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "provision_purpose_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentProvisionPurposeTransformer(FhirResourceTransformer):
    resource_type = "Consent"
    resource_component = "provision_purpose"
    view_definition = VIEW_DEFINITION
