"""FHIR Observation interpretation transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_interpretation",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "observation_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "interpretation",
            "column": [
                {
                    "name": "interpretation_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "interpretation_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationInterpretationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "interpretation", VIEW_DEFINITION)
