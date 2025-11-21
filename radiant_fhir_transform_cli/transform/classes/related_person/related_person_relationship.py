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
                    "name": "relationship_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "coding",
                    "column": [
                        {
                            "name": "relationship_coding",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class RelatedPersonRelationshipTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RelatedPerson", "relationship", VIEW_DEFINITION)
