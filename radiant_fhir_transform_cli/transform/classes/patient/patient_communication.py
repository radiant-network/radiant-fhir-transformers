"""FHIR Patient communication transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_communication",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "patient_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "communication",
            "column": [
                {
                    "name": "communication_language_coding",
                    "path": "language.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "communication_language_text",
                    "path": "language.text",
                    "type": "string",
                },
                {
                    "name": "communication_preferred",
                    "path": "preferred",
                    "type": "string",
                },
            ],
        },
    ],
}


class PatientCommunicationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "communication", VIEW_DEFINITION)
