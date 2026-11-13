"""FHIR Observation effective_timing_repeat_when transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_effective_timing_repeat_when",
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
            "forEachOrNull": "effectiveTiming.repeat.when",
            "column": [
                {
                    "name": "effective_timing_repeat_when",
                    "path": "$this",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationEffectiveTimingRepeatWhenTransformer(FhirResourceTransformer):
    resource_type = "Observation"
    resource_component = "effective_timing_repeat_when"
    view_definition = VIEW_DEFINITION
