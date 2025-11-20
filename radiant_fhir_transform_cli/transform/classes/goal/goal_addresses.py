"""FHIR Goal addresses transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_addresses",
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
                    "name": "goal_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "addresses",
            "column": [
                {
                    "name": "addresses_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "addresses_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "addresses_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class GoalAddressesTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "addresses", VIEW_DEFINITION)
