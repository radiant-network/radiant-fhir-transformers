"""FHIR Procedure report transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_report",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "procedure_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "report",
            "column": [
                {
                    "name": "report_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "report_type", "path": "type", "type": "string"},
                {"name": "report_display", "path": "display", "type": "string"},
            ],
        },
    ],
}


class ProcedureReportTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "report", VIEW_DEFINITION)
