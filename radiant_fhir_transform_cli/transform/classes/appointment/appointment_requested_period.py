"""FHIR Appointment requested_period transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_requested_period",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
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
                    "name": "appointment_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "requestedPeriod",
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
    resource_type = "Appointment"
    resource_component = "requested_period"
    view_definition = VIEW_DEFINITION
