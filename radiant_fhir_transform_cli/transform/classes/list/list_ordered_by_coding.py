"""FHIR List ordered_by_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "List",
    "name": "list_ordered_by_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "list_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "orderedBy.coding",
            "column": [
                {
                    "name": "ordered_by_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "ordered_by_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "ordered_by_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ListOrderedByCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("List", "ordered_by_coding", VIEW_DEFINITION)
