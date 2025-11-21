"""FHIR CarePlan replaces transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_replaces",
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
            "forEachOrNull": "replaces",
            "column": [
                {
                    "name": "replaces_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "replaces_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "replaces_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanReplacesTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "replaces", VIEW_DEFINITION)
