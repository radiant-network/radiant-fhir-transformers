"""FHIR CareTeam transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CareTeam",
    "name": "care_team",
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
                    "name": "name",
                    "path": "name",
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
                    "name": "period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class CareTeamTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CareTeam", None, VIEW_DEFINITION)
