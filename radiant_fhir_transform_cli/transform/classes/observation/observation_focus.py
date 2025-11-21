"""FHIR Observation focus transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_focus",
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
            "forEachOrNull": "focus",
            "column": [
                {
                    "name": "focus_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "focus_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "focus_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationFocusTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "focus", VIEW_DEFINITION)
