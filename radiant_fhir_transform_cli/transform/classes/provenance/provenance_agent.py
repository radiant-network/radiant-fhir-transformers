"""FHIR Provenance agent transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Provenance",
    "name": "provenance_agent",
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
            "forEach": "agent",
            "column": [
                {
                    "name": "agent_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "agent_role",
                    "path": "role",
                    "type": "string",
                },
                {
                    "name": "agent_who_reference",
                    "path": "who.reference",
                    "type": "string",
                },
                {
                    "name": "agent_who_type",
                    "path": "who.type",
                    "type": "string",
                },
                {
                    "name": "agent_who_display",
                    "path": "who.display",
                    "type": "string",
                },
                {
                    "name": "agent_on_behalf_of_reference",
                    "path": "onBehalfOf.reference",
                    "type": "string",
                },
                {
                    "name": "agent_on_behalf_of_type",
                    "path": "onBehalfOf.type",
                    "type": "string",
                },
                {
                    "name": "agent_on_behalf_of_display",
                    "path": "onBehalfOf.display",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "type.coding",
                    "column": [
                        {
                            "name": "agent_type_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "agent_type_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ProvenanceAgentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Provenance", "agent", VIEW_DEFINITION)
