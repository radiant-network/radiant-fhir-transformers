"""FHIR Specimen collection_method_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_collection_method_coding",
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
                    "name": "specimen_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "collection.method.coding",
            "column": [
                {
                    "name": "collection_method_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "collection_method_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "collection_method_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenCollectionMethodCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Specimen", "collection_method_coding", VIEW_DEFINITION
        )
