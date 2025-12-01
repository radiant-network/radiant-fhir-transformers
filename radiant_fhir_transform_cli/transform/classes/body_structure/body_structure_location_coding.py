"""FHIR BodyStructure location_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "BodyStructure",
    "name": "body_structure_location_coding",
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
            "forEachOrNull": "location.coding",
            "column": [
                {
                    "name": "location_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "location_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "location_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class BodyStructureLocationCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("BodyStructure", "location_coding", VIEW_DEFINITION)
