"""FHIR Appointment supporting_information transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Appointment",
    "name": "appointment_supporting_information",
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
            "forEach": "supportingInformation",
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
    def __init__(self):
        super().__init__(
            "Appointment", "supporting_information", VIEW_DEFINITION
        )
