"""FHIR RelatedPerson relationship transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "RelatedPerson",
    "name": "related_person_relationship",
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
                    "name": "related_person_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "relationship",
            "column": [
                {
                    "name": "relationship_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "relationship_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class RelatedPersonRelationshipTransformer(FhirResourceTransformer):
    resource_type = "RelatedPerson"
    resource_component = "relationship"
    view_definition = VIEW_DEFINITION
