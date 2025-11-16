"""FHIR Coverage relationship_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_relationship_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "coverage_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "relationship.coding",
            "column": [
                {
                    "name": "relationship_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "relationship_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "relationship_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class CoverageRelationshipCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Coverage", "relationship_coding", VIEW_DEFINITION)
