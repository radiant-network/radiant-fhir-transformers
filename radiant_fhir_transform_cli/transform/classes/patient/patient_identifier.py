"""FHIR Patient identifier transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_identifier",
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
            "forEachOrNull": "identifier",
            "column": [
                {
                    "name": "identifier_use",
                    "path": "use",
                    "type": "string",
                },
                {
                    "name": "identifier_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "identifier_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "identifier_value",
                    "path": "value",
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
            "select": [
                {
                    "forEachOrNull": "value.extension",
                    "column": [
                        {
                            "name": "identifier_value_extension",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class PatientIdentifierTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "identifier", VIEW_DEFINITION)
