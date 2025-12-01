"""FHIR Appointment requested_period transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_requested_period",
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
            "forEach": "requestedPeriod",
            "column": [
                {
                    "name": "requested_period_start",
                    "path": "start",
                    "type": "dateTime",
                },
                {
                    "name": "requested_period_end",
                    "path": "end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class AppointmentRequestedPeriodTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Appointment", "requested_period", VIEW_DEFINITION)
