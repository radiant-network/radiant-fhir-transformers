"""FHIR DocumentReference type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_type_coding",
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
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "type.coding",
            "column": [
                {
                    "name": "type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceTypeCodingTransformer(FhirResourceTransformer):
    resource_type = "DocumentReference"
    resource_component = "type_coding"
    view_definition = VIEW_DEFINITION
