"""FHIR CarePlan based_on transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_based_on",
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
            "forEach": "basedOn",
            "column": [
                {
                    "name": "based_on_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "based_on_display",
                    "path": "display",
                    "type": "string",
                },
                {"name": "based_on_type", "path": "type", "type": "string"},
            ],
        },
    ],
}


class CarePlanBasedOnTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "based_on", VIEW_DEFINITION)
