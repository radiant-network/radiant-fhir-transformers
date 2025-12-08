"""FHIR DocumentReference content transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_content",
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
            "forEachOrNull": "content",
            "column": [
                {
                    "name": "content_attachment_content_type",
                    "path": "attachment.contentType",
                    "type": "string",
                },
                {
                    "name": "content_attachment_language",
                    "path": "attachment.language",
                    "type": "string",
                },
                {
                    "name": "content_attachment_url",
                    "path": "attachment.url",
                    "type": "string",
                },
                {
                    "name": "content_attachment_size",
                    "path": "attachment.size",
                    "type": "integer",
                },
                {
                    "name": "content_attachment_title",
                    "path": "attachment.title",
                    "type": "string",
                },
                {
                    "name": "content_attachment_creation",
                    "path": "attachment.creation",
                    "type": "dateTime",
                },
                {
                    "name": "content_format_system",
                    "path": "format.system",
                    "type": "string",
                },
                {
                    "name": "content_format_code",
                    "path": "format.code",
                    "type": "string",
                },
                {
                    "name": "content_format_display",
                    "path": "format.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceContentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DocumentReference", "content", VIEW_DEFINITION)
