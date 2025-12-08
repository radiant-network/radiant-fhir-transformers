"""FHIR Patient telecom transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_telecom",
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
                    "name": "patient_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "telecom",
            "column": [
                {
                    "name": "telecom_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "telecom_value",
                    "path": "value",
                    "type": "string",
                },
                {
                    "name": "telecom_use",
                    "path": "use",
                    "type": "string",
                },
                {
                    "name": "telecom_rank",
                    "path": "rank",
                    "type": "integer",
                },
                {
                    "name": "telecom_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "telecom_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class PatientTelecomTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "telecom", VIEW_DEFINITION)
