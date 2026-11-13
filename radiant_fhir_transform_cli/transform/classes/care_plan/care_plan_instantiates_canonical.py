"""FHIR CarePlan instantiates_canonical transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_instantiates_canonical",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
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
            "forEachOrNull": "instantiatesCanonical",
            "column": [
                {
                    "name": "instantiates_canonical",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanInstantiatesCanonicalTransformer(FhirResourceTransformer):
    resource_type = "CarePlan"
    resource_component = "instantiates_canonical"
    view_definition = VIEW_DEFINITION
