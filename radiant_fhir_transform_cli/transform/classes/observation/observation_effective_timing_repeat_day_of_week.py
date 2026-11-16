"""FHIR Observation effective_timing_repeat_day_of_week transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_effective_timing_repeat_day_of_week",
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
                    "name": "observation_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "effectiveTiming.repeat.dayOfWeek",
            "column": [
                {
                    "name": "effective_timing_repeat_day_of_week",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationEffectiveTimingRepeatDayOfWeekTransformer(FhirResourceTransformer):
    resource_type = "Observation"
    resource_component = "effective_timing_repeat_day_of_week"
    view_definition = VIEW_DEFINITION
