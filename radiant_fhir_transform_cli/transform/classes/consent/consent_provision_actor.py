"""FHIR Consent provision_actor transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_actor",
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
            "forEachOrNull": "provision.actor",
            "column": [
                {
                    "name": "provision_actor_role_text",
                    "path": "role.text",
                    "type": "string",
                },
                {
                    "name": "provision_actor_reference_reference",
                    "path": "reference.reference",
                    "type": "string",
                },
                {
                    "name": "provision_actor_reference_type",
                    "path": "reference.type",
                    "type": "string",
                },
                {
                    "name": "provision_actor_reference_display",
                    "path": "reference.display",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "role.coding",
                    "column": [
                        {
                            "name": "provision_actor_role_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "provision_actor_role_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ConsentProvisionActorTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_actor", VIEW_DEFINITION)
