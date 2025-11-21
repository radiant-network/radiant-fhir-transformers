"""FHIR Specimen request transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_request",
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
                    "name": "specimen_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "request",
            "column": [
                {
                    "name": "request_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "request_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "request_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenRequestTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "request", VIEW_DEFINITION)
