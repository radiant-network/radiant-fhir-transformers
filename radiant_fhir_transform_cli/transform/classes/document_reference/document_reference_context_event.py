"""FHIR DocumentReference context_event transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_context_event",
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
            "forEach": "context.event",
            "column": [
                {
                    "name": "context_event_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "context_event_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceContextEventTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("DocumentReference", "context_event", VIEW_DEFINITION)
