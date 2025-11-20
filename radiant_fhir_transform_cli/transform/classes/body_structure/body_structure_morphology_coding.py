"""FHIR BodyStructure morphology_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "BodyStructure",
    "name": "body_structure_morphology_coding",
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
            "forEach": "morphology.coding",
            "column": [
                {
                    "name": "morphology_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "morphology_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "morphology_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class BodyStructureMorphologyCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("BodyStructure", "morphology_coding", VIEW_DEFINITION)
