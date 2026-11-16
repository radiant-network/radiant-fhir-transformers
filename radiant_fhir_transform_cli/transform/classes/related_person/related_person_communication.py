"""FHIR RelatedPerson communication transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "RelatedPerson",
    "name": "related_person_communication",
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
                    "name": "related_person_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "communication",
            "column": [
                {
                    "name": "communication_language_coding",
                    "path": "language.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "communication_language_text",
                    "path": "language.text",
                    "type": "string",
                },
                {
                    "name": "communication_preferred",
                    "path": "preferred",
                    "type": "string",
                },
            ],
        },
    ],
}


class RelatedPersonCommunicationTransformer(FhirResourceTransformer):
    resource_type = "RelatedPerson"
    resource_component = "communication"
    view_definition = VIEW_DEFINITION
