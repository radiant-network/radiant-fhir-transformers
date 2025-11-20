"""FHIR CarePlan instantiates_uri transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_instantiates_uri",
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
            "forEach": "instantiatesUri",
            "column": [
                {
                    "name": "instantiates_uri",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanInstantiatesUriTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "instantiates_uri", VIEW_DEFINITION)
