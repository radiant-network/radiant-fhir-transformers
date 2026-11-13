"""FHIR RequestGroup instantiates_canonical transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "RequestGroup",
    "name": "request_group_instantiates_canonical",
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
                    "name": "request_group_id",
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


class RequestGroupInstantiatesCanonicalTransformer(FhirResourceTransformer):
    resource_type = "RequestGroup"
    resource_component = "instantiates_canonical"
    view_definition = VIEW_DEFINITION
