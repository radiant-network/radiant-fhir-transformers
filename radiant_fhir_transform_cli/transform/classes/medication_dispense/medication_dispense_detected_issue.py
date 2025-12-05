"""FHIR MedicationDispense detected_issue transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_detected_issue",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "medication_dispense_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "detectedIssue",
            "column": [
                {
                    "name": "detected_issue_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "detected_issue_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "detected_issue_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class MedicationDispenseDetectedIssueTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "MedicationDispense", "detected_issue", VIEW_DEFINITION
        )
