"""FHIR MedicationDispense performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_performer",
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
            "forEach": "performer",
            "column": [
                {
                    "name": "performer_function_coding",
                    "path": "function.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "performer_function_text",
                    "path": "function.text",
                    "type": "string",
                },
                {
                    "name": "performer_actor_reference",
                    "path": "actor.reference",
                    "type": "string",
                },
                {
                    "name": "performer_actor_type",
                    "path": "actor.type",
                    "type": "string",
                },
                {
                    "name": "performer_actor_display",
                    "path": "actor.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispensePerformerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "performer", VIEW_DEFINITION)
