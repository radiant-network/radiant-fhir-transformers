"""FHIR Patient general_practitioner transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_general_practitioner",
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
                    "name": "patient_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "generalPractitioner",
            "column": [
                {
                    "name": "general_practitioner_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "general_practitioner_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "general_practitioner_identifier",
                    "path": "identifier",
                    "type": "string",
                },
                {
                    "name": "general_practitioner_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class PatientGeneralPractitionerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "general_practitioner", VIEW_DEFINITION)
