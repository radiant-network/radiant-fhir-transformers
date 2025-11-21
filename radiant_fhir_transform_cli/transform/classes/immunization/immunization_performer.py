"""FHIR Immunization performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_performer",
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
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "performer",
            "column": [
                {
                    "name": "performer_function_text",
                    "path": "function.text",
                    "type": "string",
                },
                {
                    "name": "performer_actor_reference",
                    "path": "actor.reference",
                    "type": "string",
                },
                {
                    "name": "performer_actor_type",
                    "path": "actor.type",
                    "type": "string",
                },
                {
                    "name": "performer_actor_display",
                    "path": "actor.display",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "function.coding",
                    "column": [
                        {
                            "name": "performer_function_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "performer_function_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ImmunizationPerformerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "performer", VIEW_DEFINITION)
