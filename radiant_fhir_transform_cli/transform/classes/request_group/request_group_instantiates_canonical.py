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
    def __init__(self):
        super().__init__(
            "RequestGroup", "instantiates_canonical", VIEW_DEFINITION
        )
