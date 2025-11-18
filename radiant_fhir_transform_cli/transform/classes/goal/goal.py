"""FHIR Goal transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal",
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
                    "name": "lifecycle_status",
                    "path": "lifecycleStatus",
                    "type": "string",
                },
                {
                    "name": "achievement_status_text",
                    "path": "achievementStatus.text",
                    "type": "string",
                },
                {
                    "name": "priority_text",
                    "path": "priority.text",
                    "type": "string",
                },
                {
                    "name": "description_text",
                    "path": "description.text",
                    "type": "string",
                },
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
                {"name": "start_date", "path": "startDate", "type": "dateTime"},
                {
                    "name": "start_codeable_concept_text",
                    "path": "startCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "status_date",
                    "path": "statusDate",
                    "type": "dateTime",
                },
                {
                    "name": "status_reason",
                    "path": "statusReason",
                    "type": "string",
                },
                {
                    "name": "expressed_by_reference",
                    "path": "expressedBy.reference",
                    "type": "string",
                },
                {
                    "name": "expressed_by_type",
                    "path": "expressedBy.type",
                    "type": "string",
                },
                {
                    "name": "expressed_by_display",
                    "path": "expressedBy.display",
                    "type": "string",
                },
            ]
        }
    ],
}


class GoalTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", None, VIEW_DEFINITION)
