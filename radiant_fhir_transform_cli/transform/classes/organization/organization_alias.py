"""FHIR Organization alias transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Organization",
    "name": "organization_alias",
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
            "forEachOrNull": "alias",
            "column": [
                {
                    "name": "alias",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class OrganizationAliasTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Organization", "alias", VIEW_DEFINITION)
