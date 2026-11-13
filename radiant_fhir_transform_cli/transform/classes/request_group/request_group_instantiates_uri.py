"""FHIR RequestGroup instantiates_uri transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "RequestGroup",
    "name": "request_group_instantiates_uri",
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
            "forEachOrNull": "instantiatesUri",
            "column": [
                {
                    "name": "instantiates_uri",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class RequestGroupInstantiatesUriTransformer(FhirResourceTransformer):
    resource_type = "RequestGroup"
    resource_component = "instantiates_uri"
    view_definition = VIEW_DEFINITION
