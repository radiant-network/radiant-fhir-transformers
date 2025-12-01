"""FHIR CarePlan instantiates_canonical transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_instantiates_canonical",
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
            "forEach": "instantiatesCanonical",
            "column": [
                {
                    "name": "instantiates_canonical",
                    "path": "$this",
                    "type": "string",
                }
            ],
        },
    ],
}


class CarePlanInstantiatesCanonicalTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "instantiates_canonical", VIEW_DEFINITION)
