"""FHIR CarePlan supporting_info transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_supporting_info",
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
            "forEach": "supportingInfo",
            "column": [
                {
                    "name": "supporting_info_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "supporting_info_display",
                    "path": "display",
                    "type": "string",
                },
                {
                    "name": "supporting_info_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanSupportingInfoTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "supporting_info", VIEW_DEFINITION)
