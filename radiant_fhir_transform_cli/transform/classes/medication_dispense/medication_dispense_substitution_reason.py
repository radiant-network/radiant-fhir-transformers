"""FHIR MedicationDispense substitution_reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_substitution_reason",
    "status": "active",
    "constant": [{"name": "id_hash", "valueString": "hash_row()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_hash", "type": "string"},
                {
                    "name": "medication_dispense_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "substitution.reason",
            "column": [
                {
                    "name": "substitution_reason_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseSubstitutionReasonTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "substitution_reason", VIEW_DEFINITION)
