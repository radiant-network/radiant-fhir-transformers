"""FHIR Specimen parent transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_parent",
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
            "forEachOrNull": "parent",
            "column": [
                {
                    "name": "parent_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "parent_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "parent_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenParentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "parent", VIEW_DEFINITION)
