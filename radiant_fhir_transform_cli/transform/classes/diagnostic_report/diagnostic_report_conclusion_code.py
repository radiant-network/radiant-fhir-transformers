"""FHIR DiagnosticReport conclusion_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_conclusion_code",
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
            "forEach": "conclusionCode",
            "column": [
                {
                    "name": "conclusion_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "conclusion_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class DiagnosticReportConclusionCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "conclusion_code", VIEW_DEFINITION)
