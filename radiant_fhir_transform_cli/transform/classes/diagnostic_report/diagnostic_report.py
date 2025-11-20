"""FHIR DiagnosticReport transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "effective_date_time",
                    "path": "effectiveDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "effective_period_start",
                    "path": "effectivePeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "effective_period_stop",
                    "path": "effectivePeriod.stop",
                    "type": "dateTime",
                },
                {
                    "name": "issued",
                    "path": "issued",
                    "type": "dateTime",
                },
                {
                    "name": "conclusion",
                    "path": "conclusion",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class DiagnosticReportTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", None, VIEW_DEFINITION)
