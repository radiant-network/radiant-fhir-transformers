"""FHIR Observation derived_from transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_derived_from",
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
            "forEach": "derivedFrom",
            "column": [
                {
                    "name": "derived_from_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "derived_from_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "derived_from_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationDerivedFromTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "derived_from", VIEW_DEFINITION)
