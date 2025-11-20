"""FHIR List empty_reason_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "List",
    "name": "list_empty_reason_coding",
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
                    "name": "list_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "emptyReason.coding",
            "column": [
                {
                    "name": "empty_reason_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "empty_reason_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "empty_reason_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ListEmptyReasonCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("List", "empty_reason_coding", VIEW_DEFINITION)
