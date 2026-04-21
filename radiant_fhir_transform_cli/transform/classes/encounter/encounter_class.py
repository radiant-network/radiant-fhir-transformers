"""FHIR Encounter class transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_class",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
                {
                    "name": "class_code",
                    "path": "class.code",
                    "type": "string",
                },
                {
                    "name": "class_display",
                    "path": "class.display",
                    "type": "string",
                },
                {
                    "name": "class_system",
                    "path": "class.system",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterClassTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "class", VIEW_DEFINITION)
