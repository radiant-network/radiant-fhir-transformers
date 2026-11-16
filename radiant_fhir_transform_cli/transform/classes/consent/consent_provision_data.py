"""FHIR Consent provision_data transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_provision_data",
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
            "forEachOrNull": "provision.data",
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
    resource_type = "Consent"
    resource_component = "provision_data"
    view_definition = VIEW_DEFINITION
