"""FHIR CarePlan based_on transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_based_on",
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
            "forEachOrNull": "basedOn",
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
                {
                    "name": "based_on_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanBasedOnTransformer(FhirResourceTransformer):
    resource_type = "CarePlan"
    resource_component = "based_on"
    view_definition = VIEW_DEFINITION
