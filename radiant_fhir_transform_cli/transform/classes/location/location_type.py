"""FHIR Location type transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Location",
    "name": "location_type",
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
                    "name": "location_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "type",
            "column": [
                {
                    "name": "type_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "type_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "type_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "type_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class LocationTypeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Location", "type", VIEW_DEFINITION)
