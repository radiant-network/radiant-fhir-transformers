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
            "select": [
                {
                    "forEachOrNull": "language.coding",
                    "column": [
                        {
                            "name": "communication_language_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "communication_language_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "communication_language_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class RelatedPersonCommunicationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RelatedPerson", "communication", VIEW_DEFINITION)
