"""FHIR CarePlan activity transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CarePlan",
    "name": "care_plan_activity",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "care_plan_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "activity",
            "column": [
                {
                    "name": "activity_outcome_codeable_concept",
                    "path": "outcomeCodeableConcept",
                    "type": "string",
                },
                {
                    "name": "activity_outcome_reference",
                    "path": "outcomeReference",
                    "type": "string",
                },
                {
                    "name": "activity_progress",
                    "path": "progress",
                    "type": "string",
                },
                {
                    "name": "activity_reference_reference",
                    "path": "reference.reference",
                    "type": "string",
                },
                {
                    "name": "activity_reference_display",
                    "path": "reference.display",
                    "type": "string",
                },
                {
                    "name": "activity_reference_type",
                    "path": "reference.type",
                    "type": "string",
                },
                {
                    "name": "activity_detail_kind",
                    "path": "detail.kind",
                    "type": "string",
                },
                {
                    "name": "activity_detail_instantiates_canonical",
                    "path": "detail.instantiatesCanonical",
                    "type": "string",
                },
                {
                    "name": "activity_detail_instantiates_uri",
                    "path": "detail.instantiatesUri",
                    "type": "string",
                },
                {
                    "name": "activity_detail_code_coding",
                    "path": "detail.code.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "activity_detail_code_text",
                    "path": "detail.code.text",
                    "type": "string",
                },
                {
                    "name": "activity_detail_reason_code",
                    "path": "detail.reasonCode",
                    "type": "string",
                },
                {
                    "name": "activity_detail_reason_reference",
                    "path": "detail.reasonReference",
                    "type": "string",
                },
                {
                    "name": "activity_detail_goal",
                    "path": "detail.goal",
                    "type": "string",
                },
                {
                    "name": "activity_detail_status",
                    "path": "detail.status",
                    "type": "string",
                },
                {
                    "name": "activity_detail_status_reason_coding",
                    "path": "detail.statusReason.coding",
                    "type": "string",
                },
                {
                    "name": "activity_detail_status_reason_text",
                    "path": "detail.statusReason.text",
                    "type": "string",
                },
                {
                    "name": "activity_detail_do_not_perform",
                    "path": "detail.doNotPerform",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_event",
                    "path": "detail.scheduledTiming.event",
                    "type": "dateTime",
                },
                {
                    "name": "activity_detail_scheduled_timing_code",
                    "path": "detail.scheduledTiming.code",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_duration_value",
                    "path": "detail.scheduledTiming.repeat.boundsDuration.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_duration_comparator",
                    "path": "detail.scheduledTiming.repeat.boundsDuration.comparator",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_duration_unit",
                    "path": "detail.scheduledTiming.repeat.boundsDuration.unit",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_duration_system",
                    "path": "detail.scheduledTiming.repeat.boundsDuration.system",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_duration_code",
                    "path": "detail.scheduledTiming.repeat.boundsDuration.code",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_low_value",
                    "path": "detail.scheduledTiming.repeat.boundsRange.low.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_low_unit",
                    "path": "detail.scheduledTiming.repeat.boundsRange.low.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_low_system",
                    "path": "detail.scheduledTiming.repeat.boundsRange.low.system",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_low_code",
                    "path": "detail.scheduledTiming.repeat.boundsRange.low.code",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_high_value",
                    "path": "detail.scheduledTiming.repeat.boundsRange.high.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_high_unit",
                    "path": "detail.scheduledTiming.repeat.boundsRange.high.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_high_system",
                    "path": "detail.scheduledTiming.repeat.boundsRange.high.system",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_range_high_code",
                    "path": "detail.scheduledTiming.repeat.boundsRange.high.code",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_period_start",
                    "path": "detail.scheduledTiming.repeat.boundsPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_bounds_period_end",
                    "path": "detail.scheduledTiming.repeat.boundsPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_count",
                    "path": "detail.scheduledTiming.repeat.count",
                    "type": "integer",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_count_max",
                    "path": "detail.scheduledTiming.repeat.countMax",
                    "type": "integer",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_duration",
                    "path": "detail.scheduledTiming.repeat.duration",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_duration_max",
                    "path": "detail.scheduledTiming.repeat.durationMax",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_duration_unit",
                    "path": "detail.scheduledTiming.repeat.durationUnit",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_frequency",
                    "path": "detail.scheduledTiming.repeat.frequency",
                    "type": "integer",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_frequency_max",
                    "path": "detail.scheduledTiming.repeat.frequencyMax",
                    "type": "integer",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_period",
                    "path": "detail.scheduledTiming.repeat.duration",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_period_max",
                    "path": "detail.scheduledTiming.repeat.periodMax",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_period_unit",
                    "path": "detail.scheduledTiming.repeat.periodUnit",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_day_of_week",
                    "path": "detail.scheduledTiming.repeat.dayOfWeek",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_time_of_day",
                    "path": "detail.scheduledTiming.repeat.timeOfDay",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_when",
                    "path": "detail.scheduledTiming.repeat.when",
                    "type": "string",
                },
                {
                    "name": "activity_detail_scheduled_timing_repeat_offset",
                    "path": "detail.scheduledTiming.repeat.offset",
                    "type": "integer",
                },
                {
                    "name": "activity_detail_scheduled_period_start",
                    "path": "detail.scheduledPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "activity_detail_scheduled_period_end",
                    "path": "detail.scheduledPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "activity_detail_scheduled_string",
                    "path": "detail.scheduledString",
                    "type": "string",
                },
                {
                    "name": "activity_detail_location_reference",
                    "path": "detail.location.reference",
                    "type": "string",
                },
                {
                    "name": "activity_detail_location_type",
                    "path": "detail.location.type",
                    "type": "string",
                },
                {
                    "name": "activity_detail_location_display",
                    "path": "detail.location.display",
                    "type": "string",
                },
                {
                    "name": "activity_detail_performer",
                    "path": "detail.performer",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "activity_detail_product_codeable_concept_text",
                    "path": "detail.productCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "activity_detail_product_codeable_concept_coding",
                    "path": "detail.productCodeableConcept.coding",
                    "type": "string",
                },
                {
                    "name": "activity_detail_product_reference_reference",
                    "path": "detail.productReference.reference",
                    "type": "string",
                },
                {
                    "name": "activity_detail_product_reference_display",
                    "path": "detail.productReference.display",
                    "type": "string",
                },
                {
                    "name": "activity_detail_product_reference_type",
                    "path": "detail.productReference.type",
                    "type": "string",
                },
                {
                    "name": "activity_detail_daily_amount_value",
                    "path": "detail.dailyAmount.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_daily_amount_unit",
                    "path": "detail.dailyAmount.unit",
                    "type": "string",
                },
                {
                    "name": "activity_detail_daily_amount_system",
                    "path": "detail.dailyAmount.system",
                    "type": "string",
                },
                {
                    "name": "activity_detail_daily_amount_code",
                    "path": "detail.dailyAmount.code",
                    "type": "string",
                },
                {
                    "name": "activity_detail_quantity_value",
                    "path": "detail.quantity.value",
                    "type": "string",
                },
                {
                    "name": "activity_detail_quantity_unit",
                    "path": "detail.quantity.unit",
                    "type": "string",
                },
                {
                    "name": "activity_detail_quantity_system",
                    "path": "detail.quantity.system",
                    "type": "string",
                },
                {
                    "name": "activity_detail_quantity_code",
                    "path": "detail.quantity.code",
                    "type": "string",
                },
                {
                    "name": "activity_detail_description",
                    "path": "detail.description",
                    "type": "string",
                },
            ],
        },
    ],
}


class CarePlanActivityTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CarePlan", "activity", VIEW_DEFINITION)
