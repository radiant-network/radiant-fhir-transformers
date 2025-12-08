"""FHIR RelatedPerson name transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "RelatedPerson",
    "name": "related_person_name",
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
            "forEachOrNull": "name",
            "column": [
                {
                    "name": "name_use",
                    "path": "use",
                    "type": "string",
                },
                {
                    "name": "name_text",
                    "path": "text",
                    "type": "string",
                },
                {
                    "name": "name_family",
                    "path": "family",
                    "type": "string",
                },
                {
                    "name": "name_prefix",
                    "path": "prefix",
                    "type": "string",
                },
                {
                    "name": "name_suffix",
                    "path": "suffix",
                    "type": "string",
                },
                {
                    "name": "name_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "name_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "given",
                    "column": [
                        {
                            "name": "name_given",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class RelatedPersonNameTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RelatedPerson", "name", VIEW_DEFINITION)
