"""FHIR Organization transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Organization",
    "name": "organization",
    "status": "active",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id", "type": "string"},
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {"name": "active", "path": "active", "type": "string"},
                {"name": "name", "path": "name", "type": "string"},
                {
                    "name": "part_of_reference",
                    "path": "partOf.reference",
                    "type": "string",
                },
                {
                    "name": "part_of_type",
                    "path": "partOf.type",
                    "type": "string",
                },
                {
                    "name": "part_of_display",
                    "path": "partOf.display",
                    "type": "string",
                },
            ]
        }
    ],
}


class OrganizationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Organization", None, VIEW_DEFINITION)
