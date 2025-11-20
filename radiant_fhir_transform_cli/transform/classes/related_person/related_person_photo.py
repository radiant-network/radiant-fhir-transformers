"""FHIR RelatedPerson photo transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "RelatedPerson",
    "name": "related_person_photo",
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
            "forEach": "photo",
            "column": [
                {
                    "name": "photo_content_type",
                    "path": "contentType",
                    "type": "string",
                },
                {
                    "name": "photo_language",
                    "path": "language",
                    "type": "string",
                },
                {
                    "name": "photo_url",
                    "path": "url",
                    "type": "string",
                },
                {
                    "name": "photo_size",
                    "path": "size",
                    "type": "integer",
                },
                {
                    "name": "photo_title",
                    "path": "title",
                    "type": "string",
                },
                {
                    "name": "photo_creation",
                    "path": "creation",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class RelatedPersonPhotoTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RelatedPerson", "photo", VIEW_DEFINITION)
