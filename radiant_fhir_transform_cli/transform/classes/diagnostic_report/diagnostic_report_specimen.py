"""FHIR DiagnosticReport specimen transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_specimen",
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
                    "name": "diagnostic_report_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "specimen",
            "column": [
                {
                    "name": "specimen_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "specimen_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "specimen_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class DiagnosticReportSpecimenTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "specimen", VIEW_DEFINITION)
