"""FHIR Appointment reason_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_reason_reference",
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
            "forEachOrNull": "reasonReference",
            "column": [
                {
                    "name": "reason_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "reason_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "reason_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentReasonReferenceTransformer(FhirResourceTransformer):
    resource_type = "Appointment"
    resource_component = "reason_reference"
    view_definition = VIEW_DEFINITION
