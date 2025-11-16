"""FHIR Observation effective_timing_repeat_day_of_week transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_effective_timing_repeat_day_of_week",
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
            "forEach": "effectiveTiming.repeat.dayOfWeek",
            "column": [
                {
                    "name": "effective_timing_repeat_day_of_week",
                    "path": "$this",
                    "type": "string",
                }
            ],
        },
    ],
}


class ObservationEffectiveTimingRepeatDayOfWeekTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "Observation",
            "effective_timing_repeat_day_of_week",
            VIEW_DEFINITION,
        )
