"""FHIR MedicationDispense substitution_reason transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_substitution_reason",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        }
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
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
                    "name": "substitution_reason_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
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
    resource_type = "MedicationDispense"
    resource_component = "substitution_reason"
    view_definition = VIEW_DEFINITION
