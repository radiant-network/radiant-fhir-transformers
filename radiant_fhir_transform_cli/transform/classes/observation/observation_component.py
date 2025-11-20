"""FHIR Observation component transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation_component",
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
            "forEach": "component",
            "column": [
                {
                    "name": "component_code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "component_value_quantity_value",
                    "path": "valueQuantity.value",
                    "type": "string",
                },
                {
                    "name": "component_value_quantity_comparator",
                    "path": "valueQuantity.comparator",
                    "type": "string",
                },
                {
                    "name": "component_value_quantity_unit",
                    "path": "valueQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "component_value_quantity_system",
                    "path": "valueQuantity.system",
                    "type": "string",
                },
                {
                    "name": "component_value_quantity_code",
                    "path": "valueQuantity.code",
                    "type": "string",
                },
                {
                    "name": "component_value_codeable_concept_coding",
                    "path": "valueCodeableConcept.coding",
                    "type": "string",
                },
                {
                    "name": "component_value_codeable_concept_text",
                    "path": "valueCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "component_value_string",
                    "path": "valueString",
                    "type": "string",
                },
                {
                    "name": "component_value_boolean",
                    "path": "valueBoolean",
                    "type": "string",
                },
                {
                    "name": "component_value_integer",
                    "path": "valueInteger",
                    "type": "integer",
                },
                {
                    "name": "component_value_range_low_value",
                    "path": "valueRange.low.value",
                    "type": "string",
                },
                {
                    "name": "component_value_range_low_unit",
                    "path": "valueRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "component_value_range_low_system",
                    "path": "valueRange.low.system",
                    "type": "string",
                },
                {
                    "name": "component_value_range_low_code",
                    "path": "valueRange.low.code",
                    "type": "string",
                },
                {
                    "name": "component_value_range_high_value",
                    "path": "valueRange.high.value",
                    "type": "string",
                },
                {
                    "name": "component_value_range_high_unit",
                    "path": "valueRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "component_value_range_high_system",
                    "path": "valueRange.high.system",
                    "type": "string",
                },
                {
                    "name": "component_value_range_high_code",
                    "path": "valueRange.high.code",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_numerator_value",
                    "path": "valueRatio.numerator.value",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_numerator_comparator",
                    "path": "valueRatio.numerator.comparator",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_numerator_unit",
                    "path": "valueRatio.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_numerator_system",
                    "path": "valueRatio.numerator.system",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_numerator_code",
                    "path": "valueRatio.numerator.code",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_denominator_value",
                    "path": "valueRatio.denominator.value",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_denominator_comparator",
                    "path": "valueRatio.denominator.comparator",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_denominator_unit",
                    "path": "valueRatio.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_denominator_system",
                    "path": "valueRatio.denominator.system",
                    "type": "string",
                },
                {
                    "name": "component_value_ratio_denominator_code",
                    "path": "valueRatio.denominator.code",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_origin_value",
                    "path": "valueSampledData.origin.value",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_origin_unit",
                    "path": "valueSampledData.origin.unit",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_origin_system",
                    "path": "valueSampledData.origin.system",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_origin_code",
                    "path": "valueSampledData.origin.code",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_period",
                    "path": "valueSampledData.period",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_factor",
                    "path": "valueSampledData.factor",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_lower_limit",
                    "path": "valueSampledData.lowerLimit",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_upper_limit",
                    "path": "valueSampledData.upperLimit",
                    "type": "string",
                },
                {
                    "name": "component_value_sampled_data_dimensions",
                    "path": "valueSampledData.dimensions",
                    "type": "integer",
                },
                {
                    "name": "component_value_sampled_data_data",
                    "path": "valueSampledData.data",
                    "type": "string",
                },
                {
                    "name": "component_value_time",
                    "path": "valueTime",
                    "type": "string",
                },
                {
                    "name": "component_value_date_time",
                    "path": "valueDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "component_value_period_start",
                    "path": "valuePeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "component_value_period_end",
                    "path": "valuePeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "component_data_absent_reason_coding",
                    "path": "dataAbsentReason.coding",
                    "type": "string",
                },
                {
                    "name": "component_data_absent_reason_text",
                    "path": "dataAbsentReason.text",
                    "type": "string",
                },
                {
                    "name": "component_interpretation",
                    "path": "interpretation",
                    "type": "string",
                },
                {
                    "name": "component_reference_range",
                    "path": "referenceRange",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "code.coding",
                    "column": [
                        {
                            "name": "component_code_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "component_code_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "component_code_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ObservationComponentTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", "component", VIEW_DEFINITION)
