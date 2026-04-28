"""FHIR ServiceRequest transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request",
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
                    "name": "requisition_use",
                    "path": "requisition.use",
                    "type": "string",
                },
                {
                    "name": "requisition_type_text",
                    "path": "requisition.type.text",
                    "type": "string",
                },
                {
                    "name": "requisition_system",
                    "path": "requisition.system",
                    "type": "string",
                },
                {
                    "name": "requisition_value",
                    "path": "requisition.value",
                    "type": "string",
                },
                {
                    "name": "requisition_period_start",
                    "path": "requisition.period.start",
                    "type": "string",
                },
                {
                    "name": "requisition_period_end",
                    "path": "requisition.period.end",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "intent",
                    "path": "intent",
                    "type": "string",
                },
                {
                    "name": "priority",
                    "path": "priority",
                    "type": "string",
                },
                {
                    "name": "do_not_perform",
                    "path": "doNotPerform",
                    "type": "string",
                },
                {
                    "name": "code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "quantity_quantity_value",
                    "path": "quantityQuantity.value",
                    "type": "string",
                },
                {
                    "name": "quantity_quantity_comparator",
                    "path": "quantityQuantity.comparator",
                    "type": "string",
                },
                {
                    "name": "quantity_quantity_unit",
                    "path": "quantityQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "quantity_quantity_system",
                    "path": "quantityQuantity.system",
                    "type": "string",
                },
                {
                    "name": "quantity_quantity_code",
                    "path": "quantityQuantity.code",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_numerator_value",
                    "path": "quantityRatio.numerator.value",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_numerator_comparator",
                    "path": "quantityRatio.numerator.comparator",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_numerator_unit",
                    "path": "quantityRatio.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_numerator_system",
                    "path": "quantityRatio.numerator.system",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_numerator_code",
                    "path": "quantityRatio.numerator.code",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_denominator_value",
                    "path": "quantityRatio.denominator.value",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_denominator_comparator",
                    "path": "quantityRatio.denominator.comparator",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_denominator_unit",
                    "path": "quantityRatio.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_denominator_system",
                    "path": "quantityRatio.denominator.system",
                    "type": "string",
                },
                {
                    "name": "quantity_ratio_denominator_code",
                    "path": "quantityRatio.denominator.code",
                    "type": "string",
                },
                {
                    "name": "quantity_range_low_value",
                    "path": "quantityRange.low.value",
                    "type": "string",
                },
                {
                    "name": "quantity_range_low_unit",
                    "path": "quantityRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "quantity_range_low_system",
                    "path": "quantityRange.low.system",
                    "type": "string",
                },
                {
                    "name": "quantity_range_low_code",
                    "path": "quantityRange.low.code",
                    "type": "string",
                },
                {
                    "name": "quantity_range_high_value",
                    "path": "quantityRange.high.value",
                    "type": "string",
                },
                {
                    "name": "quantity_range_high_unit",
                    "path": "quantityRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "quantity_range_high_system",
                    "path": "quantityRange.high.system",
                    "type": "string",
                },
                {
                    "name": "quantity_range_high_code",
                    "path": "quantityRange.high.code",
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
                    "name": "occurrence_date_time",
                    "path": "occurrenceDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "occurrence_period_start",
                    "path": "occurrencePeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "occurrence_period_end",
                    "path": "occurrencePeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "occurrence_timing_event",
                    "path": "occurrenceTiming.event",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "occurrence_timing_repeat_bounds_duration_value",
                    "path": "occurrenceTiming.repeat.boundsDuration.value",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_duration_comparator",
                    "path": "occurrenceTiming.repeat.boundsDuration.comparator",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_duration_unit",
                    "path": "occurrenceTiming.repeat.boundsDuration.unit",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_duration_system",
                    "path": "occurrenceTiming.repeat.boundsDuration.system",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_duration_code",
                    "path": "occurrenceTiming.repeat.boundsDuration.code",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_low_value",
                    "path": "occurrenceTiming.repeat.boundsRange.low.value",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_low_unit",
                    "path": "occurrenceTiming.repeat.boundsRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_low_system",
                    "path": "occurrenceTiming.repeat.boundsRange.low.system",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_low_code",
                    "path": "occurrenceTiming.repeat.boundsRange.low.code",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_high_value",
                    "path": "occurrenceTiming.repeat.boundsRange.high.value",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_high_unit",
                    "path": "occurrenceTiming.repeat.boundsRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_high_system",
                    "path": "occurrenceTiming.repeat.boundsRange.high.system",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_range_high_code",
                    "path": "occurrenceTiming.repeat.boundsRange.high.code",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_period_start",
                    "path": "occurrenceTiming.repeat.boundsPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "occurrence_timing_repeat_bounds_period_end",
                    "path": "occurrenceTiming.repeat.boundsPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "occurrence_timing_repeat_count",
                    "path": "occurrenceTiming.repeat.count",
                    "type": "integer",
                },
                {
                    "name": "occurrence_timing_repeat_count_max",
                    "path": "occurrenceTiming.repeat.countMax",
                    "type": "integer",
                },
                {
                    "name": "occurrence_timing_repeat_duration",
                    "path": "occurrenceTiming.repeat.duration",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_duration_max",
                    "path": "occurrenceTiming.repeat.durationMax",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_duration_unit",
                    "path": "occurrenceTiming.repeat.durationUnit",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_frequency",
                    "path": "occurrenceTiming.repeat.frequency",
                    "type": "integer",
                },
                {
                    "name": "occurrence_timing_repeat_frequency_max",
                    "path": "occurrenceTiming.repeat.frequencyMax",
                    "type": "integer",
                },
                {
                    "name": "occurrence_timing_repeat_period",
                    "path": "occurrenceTiming.repeat.period",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_period_max",
                    "path": "occurrenceTiming.repeat.periodMax",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_period_unit",
                    "path": "occurrenceTiming.repeat.periodUnit",
                    "type": "string",
                },
                {
                    "name": "occurrence_timing_repeat_day_of_week",
                    "path": "occurrenceTiming.repeat.dayOfWeek",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "occurrence_timing_repeat_time_of_day",
                    "path": "occurrenceTiming.repeat.timeOfDay",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "occurrence_timing_repeat_when",
                    "path": "occurrenceTiming.repeat.when",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "occurrence_timing_repeat_offset",
                    "path": "occurrenceTiming.repeat.offset",
                    "type": "integer",
                },
                {
                    "name": "occurrence_timing_code_coding",
                    "path": "occurrenceTiming.code.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "occurrence_timing_code_text",
                    "path": "occurrenceTiming.code.text",
                    "type": "string",
                },
                {
                    "name": "as_needed_boolean",
                    "path": "asNeededBoolean",
                    "type": "string",
                },
                {
                    "name": "as_needed_codeable_concept_text",
                    "path": "asNeededCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "authored_on",
                    "path": "authoredOn",
                    "type": "dateTime",
                },
                {
                    "name": "requester_reference",
                    "path": "requester.reference",
                    "type": "string",
                },
                {
                    "name": "requester_type",
                    "path": "requester.type",
                    "type": "string",
                },
                {
                    "name": "requester_display",
                    "path": "requester.display",
                    "type": "string",
                },
                {
                    "name": "performer_type_text",
                    "path": "performerType.text",
                    "type": "string",
                },
                {
                    "name": "patient_instruction",
                    "path": "patientInstruction",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", None, VIEW_DEFINITION)
