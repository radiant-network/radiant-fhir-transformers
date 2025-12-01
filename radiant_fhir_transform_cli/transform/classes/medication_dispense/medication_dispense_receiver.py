"""FHIR MedicationDispense receiver transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_receiver",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "medication_dispense_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "receiver",
            "column": [
                {
                    "name": "receiver_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "receiver_type", "path": "type", "type": "string"},
                {"name": "receiver_display", "path": "display", "type": "string"},
            ],
        },
    ],
}


class MedicationDispenseReceiverTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "receiver", VIEW_DEFINITION)
