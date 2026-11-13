"""FHIR Coverage relationship_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_relationship_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
                {
                    "name": "coverage_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "relationship.coding",
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
    resource_type = "Coverage"
    resource_component = "relationship_coding"
    view_definition = VIEW_DEFINITION
