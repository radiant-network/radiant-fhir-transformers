"""FHIR Provenance entity transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_entity",
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
                    "name": "provenance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "entity",
            "column": [
                {
                    "name": "entity_role",
                    "path": "role",
                    "type": "string",
                },
                {
                    "name": "entity_what_reference",
                    "path": "what.reference",
                    "type": "string",
                },
                {
                    "name": "entity_what_type",
                    "path": "what.type",
                    "type": "string",
                },
                {
                    "name": "entity_what_display",
                    "path": "what.display",
                    "type": "string",
                },
                {
                    "name": "entity_agent",
                    "path": "agent",
                    "type": "string",
                },
            ],
        },
    ],
}


class ProvenanceEntityTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", "entity", VIEW_DEFINITION)
