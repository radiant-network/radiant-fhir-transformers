"""FHIR Appointment cancelation_reason_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_cancelation_reason_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
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
            "forEach": "cancelationReason.coding",
            "column": [
                {
                    "name": "cancelation_reason_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "cancelation_reason_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "cancelation_reason_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentCancelationReasonCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Appointment", "cancelation_reason_coding", VIEW_DEFINITION
        )
