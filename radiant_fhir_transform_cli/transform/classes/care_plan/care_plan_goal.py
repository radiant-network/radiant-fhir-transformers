"""FHIR CarePlan goal transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_goal",
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
                    "name": "care_plan_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "goal",
            "column": [
                {
                    "name": "goal_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "goal_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "goal_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanGoalTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "goal", VIEW_DEFINITION)
