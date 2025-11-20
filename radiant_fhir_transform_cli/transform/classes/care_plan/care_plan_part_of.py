"""FHIR CarePlan part_of transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_part_of",
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
            "forEach": "partOf",
            "column": [
                {
                    "name": "part_of_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "part_of_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "part_of_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanPartOfTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "part_of", VIEW_DEFINITION)
