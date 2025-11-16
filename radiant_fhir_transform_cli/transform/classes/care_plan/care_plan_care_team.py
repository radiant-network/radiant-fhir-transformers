"""FHIR CarePlan care_team transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_care_team",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "care_plan_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "careTeam",
            "column": [
                {
                    "name": "care_team_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "care_team_display",
                    "path": "display",
                    "type": "string",
                },
                {"name": "care_team_type", "path": "type", "type": "string"},
            ],
        },
    ],
}


class CarePlanCareTeamTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "care_team", VIEW_DEFINITION)
