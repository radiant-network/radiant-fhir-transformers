"""FHIR AllergyIntolerance identifier transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "AllergyIntolerance",
    "name": "allergy_intolerance_identifier",
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
                    "name": "allergy_intolerance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "identifier",
            "column": [
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
                    "name": "identifier_use",
                    "path": "use",
                    "type": "string",
                },
                {
                    "name": "identifier_period_start",
                    "path": "period.start",
                    "type": "string",
                },
                {
                    "name": "identifier_period_end",
                    "path": "period.end",
                    "type": "string",
                },
            ],
        },
    ],
}


class AllergyIntoleranceIdentifierTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("AllergyIntolerance", "identifier", VIEW_DEFINITION)
