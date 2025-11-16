"""FHIR DiagnosticReport identifier transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_identifier",
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
            "forEach": "identifier",
            "column": [
                {"name": "identifier_use", "path": "use", "type": "string"},
                {
                    "name": "identifier_system",
                    "path": "system",
                    "type": "string",
                },
                {"name": "identifier_value", "path": "value", "type": "string"},
                {
                    "name": "identifier_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "identifier_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "identifier_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class DiagnosticReportIdentifierTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "identifier", VIEW_DEFINITION)
