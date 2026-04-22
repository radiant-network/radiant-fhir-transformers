"""FHIR Encounter reason_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_reason_reference",
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
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "reasonReference",
            "column": [
                {
                    "name": "reason_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "reason_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "reason_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterReasonReferenceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "reason_reference", VIEW_DEFINITION)
