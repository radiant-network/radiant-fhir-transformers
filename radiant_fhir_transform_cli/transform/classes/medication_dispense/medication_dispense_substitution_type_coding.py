"""FHIR MedicationDispense substitution_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_substitution_type_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "medication_dispense_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "substitution.type.coding",
            "column": [
                {
                    "name": "substitution_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "substitution_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "substitution_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseSubstitutionTypeCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "MedicationDispense", "substitution_type_coding", VIEW_DEFINITION
        )
