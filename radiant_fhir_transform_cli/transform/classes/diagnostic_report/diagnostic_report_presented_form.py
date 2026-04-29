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
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
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
            "forEachOrNull": "presentedForm",
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
                    "name": "presented_form_title",
                    "path": "title",
                    "type": "string",
                },
                {
                    "name": "presented_form_creation",
                    "path": "creation",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class DiagnosticReportPresentedFormTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "presented_form", VIEW_DEFINITION)
