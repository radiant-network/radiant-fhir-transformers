"""FHIR Specimen condition transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_condition",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "specimen_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "condition",
            "column": [
                {
                    "name": "condition_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "condition_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class SpecimenConditionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "condition", VIEW_DEFINITION)
