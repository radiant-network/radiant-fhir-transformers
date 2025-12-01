"""FHIR Specimen type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_type_coding",
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
            "forEach": "type.coding",
            "column": [
                {
                    "name": "type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {"name": "type_coding_code", "path": "code", "type": "string"},
                {
                    "name": "type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenTypeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "type_coding", VIEW_DEFINITION)
