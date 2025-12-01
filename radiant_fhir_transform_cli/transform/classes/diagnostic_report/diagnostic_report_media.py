"""FHIR DiagnosticReport media transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_media",
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
            "forEach": "media",
            "column": [
                {"name": "media_comment", "path": "comment", "type": "string"},
                {
                    "name": "media_link_reference",
                    "path": "link.reference",
                    "type": "string",
                },
                {
                    "name": "media_link_display",
                    "path": "link.display",
                    "type": "string",
                },
                {
                    "name": "media_link_type",
                    "path": "link.type",
                    "type": "string",
                },
            ],
        },
    ],
}


class DiagnosticReportMediaTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "media", VIEW_DEFINITION)
