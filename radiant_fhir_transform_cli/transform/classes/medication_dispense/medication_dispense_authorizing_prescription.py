"""FHIR MedicationDispense authorizing_prescription transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_authorizing_prescription",
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
            "forEach": "authorizingPrescription",
            "column": [
                {
                    "name": "authorizing_prescription_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "authorizing_prescription_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "authorizing_prescription_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseAuthorizingPrescriptionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "authorizing_prescription", VIEW_DEFINITION)
