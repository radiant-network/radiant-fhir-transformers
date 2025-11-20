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
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "author",
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
    def __init__(self):
        super().__init__("DocumentReference", "author", VIEW_DEFINITION)
