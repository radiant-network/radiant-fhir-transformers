"""FHIR Binary transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Binary",
    "name": "binary",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "content_type",
                    "path": "contentType",
                    "type": "string",
                },
                {
                    "name": "security_context_reference",
                    "path": "securityContext.reference",
                    "type": "string",
                },
                {
                    "name": "security_context_type",
                    "path": "securityContext.type",
                    "type": "string",
                },
                {
                    "name": "security_context_display",
                    "path": "securityContext.display",
                    "type": "string",
                },
                {
                    "name": "data",
                    "path": "data",
                    "type": "string",
                },
            ],
        },
    ],
}


class BinaryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Binary", None, VIEW_DEFINITION)
