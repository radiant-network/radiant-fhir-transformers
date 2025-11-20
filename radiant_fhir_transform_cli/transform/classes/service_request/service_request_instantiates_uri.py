"""FHIR ServiceRequest instantiates_uri transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_instantiates_uri",
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
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "instantiatesUri",
            "column": [
                {
                    "name": "instantiates_uri_value",
                    "path": "value",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestInstantiatesUriTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "instantiates_uri", VIEW_DEFINITION)
