"""FHIR CarePlan transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "intent",
                    "path": "intent",
                    "type": "string",
                },
                {
                    "name": "title",
                    "path": "title",
                    "type": "string",
                },
                {
                    "name": "description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
                {
                    "name": "created",
                    "path": "created",
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
            ],
        },
    ],
}


class CarePlanTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", None, VIEW_DEFINITION)
