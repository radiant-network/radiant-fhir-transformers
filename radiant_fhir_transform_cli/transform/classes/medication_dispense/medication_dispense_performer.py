"""FHIR MedicationDispense performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_performer",
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
            "forEach": "performer",
            "column": [
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
                {
                    "name": "performer_function_text",
                    "path": "function.text",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispensePerformerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "performer", VIEW_DEFINITION)
