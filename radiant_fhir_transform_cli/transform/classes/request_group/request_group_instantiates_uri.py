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
    def __init__(self):
        super().__init__("RequestGroup", "instantiates_uri", VIEW_DEFINITION)
