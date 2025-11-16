"""FHIR DocumentReference relates_to transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_relates_to",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "relatesTo",
            "column": [
                {
                    "name": "relates_to_target_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "relates_to_target_reference",
                    "path": "target.reference",
                    "type": "string",
                },
                {
                    "name": "relates_to_target_type",
                    "path": "target.type",
                    "type": "string",
                },
                {
                    "name": "relates_to_target_display",
                    "path": "target.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceRelatesToTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DocumentReference", "relates_to", VIEW_DEFINITION)
