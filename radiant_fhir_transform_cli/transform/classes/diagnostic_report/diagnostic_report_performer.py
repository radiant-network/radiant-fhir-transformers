"""FHIR DiagnosticReport performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_performer",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "diagnostic_report_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "performer",
            "column": [
                {
                    "name": "performer_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "performer_display",
                    "path": "display",
                    "type": "string",
                },
                {"name": "performer_type", "path": "type", "type": "string"},
            ],
        },
    ],
}


class DiagnosticReportPerformerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "performer", VIEW_DEFINITION)
