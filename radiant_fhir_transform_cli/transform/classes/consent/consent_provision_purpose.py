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
            "forEach": "provision.purpose",
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
    def __init__(self):
        super().__init__("Consent", "provision_purpose", VIEW_DEFINITION)
