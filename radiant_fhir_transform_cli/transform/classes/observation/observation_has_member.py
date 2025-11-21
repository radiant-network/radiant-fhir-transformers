"""FHIR Observation has_member transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_has_member",
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
                    "name": "observation_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "hasMember",
            "column": [
                {
                    "name": "has_member_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "has_member_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "has_member_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationHasMemberTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "has_member", VIEW_DEFINITION)
