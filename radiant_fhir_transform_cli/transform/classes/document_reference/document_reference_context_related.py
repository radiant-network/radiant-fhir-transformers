"""FHIR DocumentReference context_related transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_context_related",
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
            "forEachOrNull": "context.related",
            "column": [
                {
                    "name": "context_related_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "context_related_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "context_related_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceContextRelatedTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "DocumentReference", "context_related", VIEW_DEFINITION
        )
