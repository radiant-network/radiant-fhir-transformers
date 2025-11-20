"""FHIR DiagnosticReport imaging_study transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DiagnosticReport",
    "name": "diagnostic_report_imaging_study",
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
            "forEach": "imagingStudy",
            "column": [
                {
                    "name": "imaging_study_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "imaging_study_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "imaging_study_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class DiagnosticReportImagingStudyTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DiagnosticReport", "imaging_study", VIEW_DEFINITION)
