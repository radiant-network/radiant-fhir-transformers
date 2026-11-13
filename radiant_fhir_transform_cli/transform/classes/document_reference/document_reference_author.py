"""FHIR DocumentReference author transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_author",
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
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "author",
            "column": [
                {
                    "name": "author_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "author_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "author_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceAuthorTransformer(FhirResourceTransformer):
    resource_type = "DocumentReference"
    resource_component = "author"
    view_definition = VIEW_DEFINITION
