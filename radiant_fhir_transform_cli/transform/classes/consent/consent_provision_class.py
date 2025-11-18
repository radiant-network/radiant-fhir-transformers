"""FHIR Consent provision_class transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_class",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "consent_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "provision.class",
            "column": [
                {
                    "name": "provision_class_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "provision_class_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "provision_class_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentProvisionClassTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_class", VIEW_DEFINITION)
