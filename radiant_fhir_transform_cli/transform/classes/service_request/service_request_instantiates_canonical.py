"""FHIR ServiceRequest instantiates_canonical transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_instantiates_canonical",
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
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "instantiatesCanonical",
            "column": [
                {
                    "name": "instantiates_canonical",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestInstantiatesCanonicalTransformer(FhirResourceTransformer):
    resource_type = "ServiceRequest"
    resource_component = "instantiates_canonical"
    view_definition = VIEW_DEFINITION
