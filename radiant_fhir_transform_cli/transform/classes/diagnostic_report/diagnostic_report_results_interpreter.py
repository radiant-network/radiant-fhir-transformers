"""FHIR DiagnosticReport results_interpreter transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_results_interpreter",
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
            "forEachOrNull": "resultsInterpreter",
            "column": [
                {
                    "name": "results_interpreter_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "results_interpreter_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "results_interpreter_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class DiagnosticReportResultsInterpreterTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "DiagnosticReport", "results_interpreter", VIEW_DEFINITION
        )
