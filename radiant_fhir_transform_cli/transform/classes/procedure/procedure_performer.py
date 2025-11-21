"""FHIR Procedure performer transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure_performer",
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
                    "name": "procedure_id",
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
                {
                    "name": "performer_on_behalf_of_reference",
                    "path": "onBehalfOf.reference",
                    "type": "string",
                },
                {
                    "name": "performer_on_behalf_of_type",
                    "path": "onBehalfOf.type",
                    "type": "string",
                },
                {
                    "name": "performer_on_behalf_of_display",
                    "path": "onBehalfOf.display",
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
                        {
                            "name": "performer_function_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProcedurePerformerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", "performer", VIEW_DEFINITION)
