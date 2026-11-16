"""FHIR Observation effective_timing_event transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_effective_timing_event",
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
            "forEachOrNull": "effectiveTiming.event",
            "column": [
                {
                    "name": "effective_timing_event",
                    "path": "$this",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class ObservationEffectiveTimingEventTransformer(FhirResourceTransformer):
    resource_type = "Observation"
    resource_component = "effective_timing_event"
    view_definition = VIEW_DEFINITION
