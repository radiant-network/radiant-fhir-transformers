"""FHIR RequestGroup transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "RequestGroup",
    "name": "request_group",
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
                {
                    "name": "group_identifier_type_text",
                    "path": "groupIdentifier.type.text",
                    "type": "string",
                },
                {
                    "name": "group_identifier_system",
                    "path": "groupIdentifier.system",
                    "type": "string",
                },
                {
                    "name": "group_identifier_value",
                    "path": "groupIdentifier.value",
                    "type": "string",
                },
                {
                    "name": "group_identifier_period_start",
                    "path": "groupIdentifier.period.start",
                    "type": "string",
                },
                {
                    "name": "group_identifier_period_end",
                    "path": "groupIdentifier.period.end",
                    "type": "string",
                },
                {"name": "status", "path": "status", "type": "string"},
                {"name": "intent", "path": "intent", "type": "string"},
                {"name": "priority", "path": "priority", "type": "string"},
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
                {
                    "name": "authored_on",
                    "path": "authoredOn",
                    "type": "dateTime",
                },
                {
                    "name": "author_reference",
                    "path": "author.reference",
                    "type": "string",
                },
                {
                    "name": "author_type",
                    "path": "author.type",
                    "type": "string",
                },
                {
                    "name": "author_display",
                    "path": "author.display",
                    "type": "string",
                },
            ]
        }
    ],
}


class RequestGroupTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RequestGroup", None, VIEW_DEFINITION)
