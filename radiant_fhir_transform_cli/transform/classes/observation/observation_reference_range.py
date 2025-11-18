"""FHIR Observation reference_range transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_reference_range",
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
            "forEach": "referenceRange",
            "column": [
                {
                    "name": "reference_range_low_value",
                    "path": "low.value",
                    "type": "string",
                },
                {
                    "name": "reference_range_low_unit",
                    "path": "low.unit",
                    "type": "string",
                },
                {
                    "name": "reference_range_low_system",
                    "path": "low.system",
                    "type": "string",
                },
                {
                    "name": "reference_range_low_code",
                    "path": "low.code",
                    "type": "string",
                },
                {
                    "name": "reference_range_high_value",
                    "path": "high.value",
                    "type": "string",
                },
                {
                    "name": "reference_range_high_unit",
                    "path": "high.unit",
                    "type": "string",
                },
                {
                    "name": "reference_range_high_system",
                    "path": "high.system",
                    "type": "string",
                },
                {
                    "name": "reference_range_high_code",
                    "path": "high.code",
                    "type": "string",
                },
                {
                    "name": "reference_range_type_coding",
                    "path": "type.coding",
                    "type": "string",
                },
                {
                    "name": "reference_range_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "reference_range_applies_to",
                    "path": "appliesTo",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_low_value",
                    "path": "age.low.value",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_low_unit",
                    "path": "age.low.unit",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_low_system",
                    "path": "age.low.system",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_low_code",
                    "path": "age.low.code",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_high_value",
                    "path": "age.high.value",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_high_unit",
                    "path": "age.high.unit",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_high_system",
                    "path": "age.high.system",
                    "type": "string",
                },
                {
                    "name": "reference_range_age_high_code",
                    "path": "age.high.code",
                    "type": "string",
                },
                {
                    "name": "reference_range_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationReferenceRangeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "reference_range", VIEW_DEFINITION)
