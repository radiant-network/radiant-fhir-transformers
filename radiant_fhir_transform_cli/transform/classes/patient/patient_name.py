"""FHIR Patient name transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_name",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "patient_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "name",
            "column": [
                {"name": "name_use", "path": "use", "type": "string"},
                {"name": "name_text", "path": "text", "type": "string"},
                {"name": "name_family", "path": "family", "type": "string"},
                {
                    "name": "name_given",
                    "path": "given",
                    "type": "string",
                    "collection": True,
                },
                {"name": "name_prefix", "path": "prefix", "type": "string"},
                {"name": "name_suffix", "path": "suffix", "type": "string"},
                {
                    "name": "name_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "name_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class PatientNameTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "name", VIEW_DEFINITION)
