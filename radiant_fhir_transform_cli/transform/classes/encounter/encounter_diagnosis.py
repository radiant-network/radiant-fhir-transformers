"""FHIR Encounter diagnosis transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_diagnosis",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "encounter_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "diagnosis",
            "column": [
                {
                    "name": "diagnosis_condition_reference",
                    "path": "condition.reference",
                    "type": "string",
                },
                {
                    "name": "diagnosis_condition_type",
                    "path": "condition.type",
                    "type": "string",
                },
                {
                    "name": "diagnosis_condition_display",
                    "path": "condition.display",
                    "type": "string",
                },
                {
                    "name": "diagnosis_use_coding",
                    "path": "use.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "diagnosis_use_text",
                    "path": "use.text",
                    "type": "string",
                },
                {"name": "diagnosis_rank", "path": "rank", "type": "integer"},
            ],
        },
    ],
}


class EncounterDiagnosisTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "diagnosis", VIEW_DEFINITION)
