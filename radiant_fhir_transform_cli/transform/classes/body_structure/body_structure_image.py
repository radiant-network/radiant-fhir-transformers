"""FHIR BodyStructure image transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "BodyStructure",
    "name": "body_structure_image",
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
                    "name": "body_structure_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "image",
            "column": [
                {
                    "name": "image_content_type",
                    "path": "contentType",
                    "type": "string",
                },
                {
                    "name": "image_language",
                    "path": "language",
                    "type": "string",
                },
                {
                    "name": "image_url",
                    "path": "url",
                    "type": "string",
                },
                {
                    "name": "image_size",
                    "path": "size",
                    "type": "integer",
                },
                {
                    "name": "image_title",
                    "path": "title",
                    "type": "string",
                },
                {
                    "name": "image_creation",
                    "path": "creation",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class BodyStructureImageTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("BodyStructure", "image", VIEW_DEFINITION)
