"""FHIR Observation effective_timing_code_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_effective_timing_code_coding",
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
            "forEachOrNull": "effectiveTiming.code.coding",
            "column": [
                {
                    "name": "effective_timing_code_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "effective_timing_code_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "effective_timing_code_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationEffectiveTimingCodeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "Observation", "effective_timing_code_coding", VIEW_DEFINITION
        )
