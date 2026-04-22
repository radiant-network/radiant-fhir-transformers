"""FHIR MedicationDispense substitution_responsible_party transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_substitution_responsible_party",
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
            "forEach": "substitution.responsibleParty",
            "column": [
                {
                    "name": "substitution_responsible_party_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "substitution_responsible_party_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "substitution_responsible_party_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseSubstitutionResponsiblePartyTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "MedicationDispense",
            "substitution_responsible_party",
            VIEW_DEFINITION,
        )
