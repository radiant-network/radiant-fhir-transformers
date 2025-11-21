"""FHIR DiagnosticReport result transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_result",
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
            "forEachOrNull": "result",
            "column": [
                {
                    "name": "result_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "result_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "result_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class DiagnosticReportResultTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "result", VIEW_DEFINITION)
