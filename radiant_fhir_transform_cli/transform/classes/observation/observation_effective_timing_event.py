"""FHIR Observation effective_timing_event transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_effective_timing_event",
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
            "forEach": "effectiveTiming.event",
            "column": [
                {
                    "name": "effective_timing_event",
                    "path": "$this",
                    "type": "dateTime",
                }
            ],
        },
    ],
}


class ObservationEffectiveTimingEventTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Observation", "effective_timing_event", VIEW_DEFINITION
        )
