"""FHIR Organization endpoint transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Organization",
    "name": "organization_endpoint",
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
                    "name": "organization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "endpoint",
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


class OrganizationEndpointTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Organization", "endpoint", VIEW_DEFINITION)
