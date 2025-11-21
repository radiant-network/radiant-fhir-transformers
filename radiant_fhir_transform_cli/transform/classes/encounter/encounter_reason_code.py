"""FHIR Encounter reason_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_reason_code",
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
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "reasonCode",
            "column": [
                {
                    "name": "reason_code_coding",
                    "path": "coding",
                    "type": "string",
                },
                {
                    "name": "reason_code_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterReasonCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "reason_code", VIEW_DEFINITION)
