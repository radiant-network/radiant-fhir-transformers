"""FHIR Appointment supporting_information transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_supporting_information",
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
            "forEachOrNull": "supportingInformation",
            "column": [
                {
                    "name": "supporting_information_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "supporting_information_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "supporting_information_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class AppointmentSupportingInformationTransformer(FhirResourceTransformer):
    resource_type = "Appointment"
    resource_component = "supporting_information"
    view_definition = VIEW_DEFINITION
