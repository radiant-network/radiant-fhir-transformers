"""FHIR Encounter account transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_account",
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
            "forEach": "account",
            "column": [
                {
                    "name": "account_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "account_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "account_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterAccountTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "account", VIEW_DEFINITION)
