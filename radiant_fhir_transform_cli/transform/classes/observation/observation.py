"""FHIR Observation transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Observation",
    "name": "observation",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {
                    "name": "effective_date_time",
                    "path": "effectiveDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "effective_period_start",
                    "path": "effectivePeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "effective_period_end",
                    "path": "effectivePeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "effective_timing_repeat_bounds_duration_value",
                    "path": "effectiveTiming.repeat.boundsDuration.value",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_duration_comparator",
                    "path": "effectiveTiming.repeat.boundsDuration.comparator",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_duration_unit",
                    "path": "effectiveTiming.repeat.boundsDuration.unit",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_duration_system",
                    "path": "effectiveTiming.repeat.boundsDuration.system",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_duration_code",
                    "path": "effectiveTiming.repeat.boundsDuration.code",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_low_value",
                    "path": "effectiveTiming.repeat.boundsRange.low.value",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_low_unit",
                    "path": "effectiveTiming.repeat.boundsRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_low_system",
                    "path": "effectiveTiming.repeat.boundsRange.low.system",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_low_code",
                    "path": "effectiveTiming.repeat.boundsRange.low.code",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_high_value",
                    "path": "effectiveTiming.repeat.boundsRange.high.value",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_high_unit",
                    "path": "effectiveTiming.repeat.boundsRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_high_system",
                    "path": "effectiveTiming.repeat.boundsRange.high.system",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_range_high_code",
                    "path": "effectiveTiming.repeat.boundsRange.high.code",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_bounds_period_start",
                    "path": "effectiveTiming.repeat.boundsPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "effective_timing_repeat_bounds_period_end",
                    "path": "effectiveTiming.repeat.boundsPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "effective_timing_repeat_count",
                    "path": "effectiveTiming.repeat.count",
                    "type": "integer",
                },
                {
                    "name": "effective_timing_repeat_count_max",
                    "path": "effectiveTiming.repeat.countMax",
                    "type": "integer",
                },
                {
                    "name": "effective_timing_repeat_duration",
                    "path": "effectiveTiming.repeat.duration",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_duration_max",
                    "path": "effectiveTiming.repeat.durationMax",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_duration_unit",
                    "path": "effectiveTiming.repeat.durationUnit",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_frequency",
                    "path": "effectiveTiming.repeat.frequency",
                    "type": "integer",
                },
                {
                    "name": "effective_timing_repeat_frequency_max",
                    "path": "effectiveTiming.repeat.frequencyMax",
                    "type": "integer",
                },
                {
                    "name": "effective_timing_repeat_period",
                    "path": "effectiveTiming.repeat.period",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_period_max",
                    "path": "effectiveTiming.repeat.periodMax",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_period_unit",
                    "path": "effectiveTiming.repeat.periodUnit",
                    "type": "string",
                },
                {
                    "name": "effective_timing_repeat_offset",
                    "path": "effectiveTiming.repeat.offset",
                    "type": "integer",
                },
                {
                    "name": "effective_timing_code_text",
                    "path": "effectiveTiming.code.text",
                    "type": "string",
                },
                {
                    "name": "effective_instant",
                    "path": "effectiveInstant",
                    "type": "dateTime",
                },
                {
                    "name": "issued",
                    "path": "issued",
                    "type": "dateTime",
                },
                {
                    "name": "value_quantity_value",
                    "path": "valueQuantity.value",
                    "type": "string",
                },
                {
                    "name": "value_quantity_comparator",
                    "path": "valueQuantity.comparator",
                    "type": "string",
                },
                {
                    "name": "value_quantity_unit",
                    "path": "valueQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "value_quantity_system",
                    "path": "valueQuantity.system",
                    "type": "string",
                },
                {
                    "name": "value_quantity_code",
                    "path": "valueQuantity.code",
                    "type": "string",
                },
                {
                    "name": "value_codeable_concept_text",
                    "path": "valueCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "value_string",
                    "path": "valueString",
                    "type": "string",
                },
                {
                    "name": "value_boolean",
                    "path": "valueBoolean",
                    "type": "string",
                },
                {
                    "name": "value_integer",
                    "path": "valueInteger",
                    "type": "integer",
                },
                {
                    "name": "value_range_low_value",
                    "path": "valueRange.low.value",
                    "type": "string",
                },
                {
                    "name": "value_range_low_unit",
                    "path": "valueRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "value_range_low_system",
                    "path": "valueRange.low.system",
                    "type": "string",
                },
                {
                    "name": "value_range_low_code",
                    "path": "valueRange.low.code",
                    "type": "string",
                },
                {
                    "name": "value_range_high_value",
                    "path": "valueRange.high.value",
                    "type": "string",
                },
                {
                    "name": "value_range_high_unit",
                    "path": "valueRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "value_range_high_system",
                    "path": "valueRange.high.system",
                    "type": "string",
                },
                {
                    "name": "value_range_high_code",
                    "path": "valueRange.high.code",
                    "type": "string",
                },
                {
                    "name": "value_ratio_numerator_value",
                    "path": "valueRatio.numerator.value",
                    "type": "string",
                },
                {
                    "name": "value_ratio_numerator_comparator",
                    "path": "valueRatio.numerator.comparator",
                    "type": "string",
                },
                {
                    "name": "value_ratio_numerator_unit",
                    "path": "valueRatio.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "value_ratio_numerator_system",
                    "path": "valueRatio.numerator.system",
                    "type": "string",
                },
                {
                    "name": "value_ratio_numerator_code",
                    "path": "valueRatio.numerator.code",
                    "type": "string",
                },
                {
                    "name": "value_ratio_denominator_value",
                    "path": "valueRatio.denominator.value",
                    "type": "string",
                },
                {
                    "name": "value_ratio_denominator_comparator",
                    "path": "valueRatio.denominator.comparator",
                    "type": "string",
                },
                {
                    "name": "value_ratio_denominator_unit",
                    "path": "valueRatio.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "value_ratio_denominator_system",
                    "path": "valueRatio.denominator.system",
                    "type": "string",
                },
                {
                    "name": "value_ratio_denominator_code",
                    "path": "valueRatio.denominator.code",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_origin_value",
                    "path": "valueSampledData.origin.value",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_origin_unit",
                    "path": "valueSampledData.origin.unit",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_origin_system",
                    "path": "valueSampledData.origin.system",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_origin_code",
                    "path": "valueSampledData.origin.code",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_period",
                    "path": "valueSampledData.period",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_factor",
                    "path": "valueSampledData.factor",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_lower_limit",
                    "path": "valueSampledData.lowerLimit",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_upper_limit",
                    "path": "valueSampledData.upperLimit",
                    "type": "string",
                },
                {
                    "name": "value_sampled_data_dimensions",
                    "path": "valueSampledData.dimensions",
                    "type": "integer",
                },
                {
                    "name": "value_sampled_data_data",
                    "path": "valueSampledData.data",
                    "type": "string",
                },
                {
                    "name": "value_time",
                    "path": "valueTime",
                    "type": "string",
                },
                {
                    "name": "value_date_time",
                    "path": "valueDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "value_period_start",
                    "path": "valuePeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "value_period_end",
                    "path": "valuePeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "data_absent_reason_text",
                    "path": "dataAbsentReason.text",
                    "type": "string",
                },
                {
                    "name": "body_site_text",
                    "path": "bodySite.text",
                    "type": "string",
                },
                {
                    "name": "method_text",
                    "path": "method.text",
                    "type": "string",
                },
                {
                    "name": "specimen_reference",
                    "path": "specimen.reference",
                    "type": "string",
                },
                {
                    "name": "specimen_type",
                    "path": "specimen.type",
                    "type": "string",
                },
                {
                    "name": "specimen_display",
                    "path": "specimen.display",
                    "type": "string",
                },
                {
                    "name": "device_reference",
                    "path": "device.reference",
                    "type": "string",
                },
                {
                    "name": "device_type",
                    "path": "device.type",
                    "type": "string",
                },
                {
                    "name": "device_display",
                    "path": "device.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ObservationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Observation", None, VIEW_DEFINITION)
