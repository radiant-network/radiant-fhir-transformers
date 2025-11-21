"""FHIR Location endpoint transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Location",
    "name": "location_endpoint",
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
                    "name": "location_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "endpoint",
            "column": [
                {
                    "name": "endpoint_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "endpoint_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "endpoint_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class LocationEndpointTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Location", "endpoint", VIEW_DEFINITION)
