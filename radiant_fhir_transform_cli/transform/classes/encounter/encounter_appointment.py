"""FHIR Encounter appointment transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_appointment",
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
            "forEach": "appointment",
            "column": [
                {
                    "name": "appointment_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "appointment_type", "path": "type", "type": "string"},
                {
                    "name": "appointment_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterAppointmentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "appointment", VIEW_DEFINITION)
