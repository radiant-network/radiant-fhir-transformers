"""FHIR DiagnosticReport presented_form transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_presented_form",
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
            "forEach": "presentedForm",
            "column": [
                {
                    "name": "presented_form_content_type",
                    "path": "contentType",
                    "type": "string",
                },
                {
                    "name": "presented_form_language",
                    "path": "language",
                    "type": "string",
                },
                {
                    "name": "presented_form_url",
                    "path": "url",
                    "type": "string",
                },
                {
                    "name": "presented_form_size",
                    "path": "size",
                    "type": "integer",
                },
                {
                    "name": "presented_form_hash",
                    "path": "hash",
                    "type": "string",
                },
                {
                    "name": "presented_form_title",
                    "path": "title",
                    "type": "string",
                },
                {
                    "name": "presented_form_creation",
                    "path": "url",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class DiagnosticReportPresentedFormTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "presented_form", VIEW_DEFINITION)
