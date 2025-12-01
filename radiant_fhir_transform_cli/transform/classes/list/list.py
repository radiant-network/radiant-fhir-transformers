"""FHIR List transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "List",
    "name": "list",
    "status": "active",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id", "type": "string"},
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {"name": "status", "path": "status", "type": "string"},
                {"name": "mode", "path": "mode", "type": "string"},
                {"name": "title", "path": "title", "type": "string"},
                {"name": "code_text", "path": "code.text", "type": "string"},
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {"name": "date", "path": "date", "type": "dateTime"},
                {
                    "name": "source_reference",
                    "path": "source.reference",
                    "type": "string",
                },
                {
                    "name": "source_type",
                    "path": "source.type",
                    "type": "string",
                },
                {
                    "name": "source_display",
                    "path": "source.display",
                    "type": "string",
                },
                {
                    "name": "ordered_by_text",
                    "path": "orderedBy.text",
                    "type": "string",
                },
                {
                    "name": "empty_reason_text",
                    "path": "emptyReason.text",
                    "type": "string",
                },
            ]
        }
    ],
}


class ListTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("List", None, VIEW_DEFINITION)
