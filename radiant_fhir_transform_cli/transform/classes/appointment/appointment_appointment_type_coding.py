"""FHIR Appointment appointment_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_appointment_type_coding",
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
            "forEach": "appointmentType.coding",
            "column": [
                {
                    "name": "appointment_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "appointment_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "appointment_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentAppointmentTypeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Appointment", "appointment_type_coding", VIEW_DEFINITION
        )
