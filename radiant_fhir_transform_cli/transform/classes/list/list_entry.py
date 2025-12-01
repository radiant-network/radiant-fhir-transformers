"""FHIR List entry transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "List",
    "name": "list_entry",
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
            "forEach": "entry",
            "column": [
                {
                    "name": "entry_flag_coding",
                    "path": "flag.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "entry_flag_text",
                    "path": "flag.text",
                    "type": "string",
                },
                {"name": "entry_deleted", "path": "deleted", "type": "string"},
                {"name": "entry_date", "path": "date", "type": "dateTime"},
                {
                    "name": "entry_item_reference",
                    "path": "item.reference",
                    "type": "string",
                },
                {
                    "name": "entry_item_type",
                    "path": "item.type",
                    "type": "string",
                },
                {
                    "name": "entry_item_display",
                    "path": "item.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ListEntryTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("List", "entry", VIEW_DEFINITION)
