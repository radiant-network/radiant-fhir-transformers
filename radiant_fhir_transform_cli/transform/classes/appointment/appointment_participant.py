"""FHIR Appointment participant transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_participant",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "appointment_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "participant",
            "column": [
                {
                    "name": "participant_type",
                    "path": "type",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "participant_actor_reference",
                    "path": "actor.reference",
                    "type": "string",
                },
                {
                    "name": "participant_actor_type",
                    "path": "actor.type",
                    "type": "string",
                },
                {
                    "name": "participant_actor_display",
                    "path": "actor.display",
                    "type": "string",
                },
                {
                    "name": "participant_required",
                    "path": "required",
                    "type": "string",
                },
                {
                    "name": "participant_status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "participant_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "participant_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class AppointmentParticipantTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "participant", VIEW_DEFINITION)
