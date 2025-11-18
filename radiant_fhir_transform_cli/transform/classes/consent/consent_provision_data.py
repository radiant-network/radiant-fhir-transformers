"""FHIR Consent provision_data transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_data",
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
            "forEach": "provision.data",
            "column": [
                {
                    "name": "provision_data_meaning",
                    "path": "meaning",
                    "type": "string",
                },
                {
                    "name": "provision_data_reference_reference",
                    "path": "reference.reference",
                    "type": "string",
                },
                {
                    "name": "provision_data_reference_type",
                    "path": "reference.type",
                    "type": "string",
                },
                {
                    "name": "provision_data_reference_display",
                    "path": "reference.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentProvisionDataTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "provision_data", VIEW_DEFINITION)
