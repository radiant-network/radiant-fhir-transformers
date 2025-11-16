"""FHIR RequestGroup replaces transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "RequestGroup",
    "name": "request_group_replaces",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "request_group_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "replaces",
            "column": [
                {
                    "name": "replaces_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "replaces_type", "path": "type", "type": "string"},
                {
                    "name": "replaces_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class RequestGroupReplacesTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RequestGroup", "replaces", VIEW_DEFINITION)
