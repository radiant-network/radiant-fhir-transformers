"""FHIR Organization type transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Organization",
    "name": "organization_type",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "organization_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "type",
            "column": [
                {
                    "name": "type_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "type_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class OrganizationTypeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Organization", "type", VIEW_DEFINITION)
