"""FHIR CarePlan contributor transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_contributor",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "care_plan_id", "path": "id", "type": "string"},
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "contributor_reference",
                    "path": "contributor.reference",
                    "type": "string",
                },
                {
                    "name": "contributor_display",
                    "path": "contributor.display",
                    "type": "string",
                },
                {
                    "name": "contributor_type",
                    "path": "contributor.type",
                    "type": "string",
                },
            ]
        }
    ],
}


class CarePlanContributorTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "contributor", VIEW_DEFINITION)
