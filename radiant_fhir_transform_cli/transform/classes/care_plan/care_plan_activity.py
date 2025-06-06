"""
FHIR CarePlan Activity transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "care_plan_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "activity",
        "columns": {
            "activity_outcome_codeable_concept": {
                "fhir_key": "outcomeCodeableConcept",
                "type": "str",
            },
            "activity_outcome_reference": {
                "fhir_key": "outcomeReference",
                "type": "str",
            },
            "activity_outcome_progress": {
                "fhir_key": "progress",
                "type": "str",
            },
            "activity_reference_reference": {
                "fhir_key": "reference.reference",
                "type": "str",
            },
            "activity_reference.display": {
                "fhir_key": "reference.display",
                "type": "str",
            },
            "activity_reference.type": {
                "fhir_key": "reference.type",
                "type": "str",
            },
            "activity_detail_kind": {"fhir_key": "detail.kind", "type": "str"},
            "activity_detail_instantiates_canonical": {
                "fhir_key": "detail.instantiatesCanonical",
                "type": "str",
            },
            "activity_detail_instantiates_uri": {
                "fhir_key": "detail.instantiatesUri",
                "type": "str",
            },
            "activity_detail_code_coding": {
                "fhir_key": "detail.code.coding",
                "type": "str",
            },
            "activity_detail_code_text": {
                "fhir_key": "detail.code.text",
                "type": "str",
            },
            "activity_detail_reason_code": {
                "fhir_key": "detail.reasonCode",
                "type": "str",
            },
            "activity_detail_reason_reference": {
                "fhir_key": "detail.reasonReference",
                "type": "str",
            },
            "activity_detail_goal": {"fhir_key": "detail.goal", "type": "str"},
            "activity_detail_status": {
                "fhir_key": "detail.status",
                "type": "str",
            },
            "activity_detail_status_reason": {
                "fhir_key": "detail.statusReason",
                "type": "str",
            },
            "activity_detail_do_not_perform": {
                "fhir_key": "detail.doNotPerform",
                "type": "bool",
            },
            # start Scheduled element
            # scheduledTiming
            "activity_detail_scheduled_timing_event": {
                "fhir_key": "detail.scheduledTiming.event",
                "type": "datetime",
            },
            "activity_detail_scheduled_timing_code": {
                "fhir_key": "detail.scheduledTiming.code",
                "type": "str",
            },  # this is at the end of the r4 spec but listing it here for easy tracking
            # scheduledTiming.repeat.boundsDuration
            "activity_detail_scheduled_timing_repeat_bounds_duration_value": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsDuration.value",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_duration_comparator": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsDuration.comparator",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_duration_unit": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsDuration.unit",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_duration_system": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsDuration.system",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_duration_code": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsDuration.code",
                "type": "str",
            },
            # scheduledTiming.repeat.boundsRange
            "activity_detail_scheduled_timing_repeat_bounds_range_low_value": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.low.value",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_low_unit": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.low.value",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_low_system": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.low.system",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_low_code": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.low.code",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_high_value": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.high.value",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_high_unit": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.high.value",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_high_system": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.high.system",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_bounds_range_high_code": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsRange.high.code",
                "type": "str",
            },
            # scheduledTiming.repeat.boundsPeriod
            "activity_detail_scheduled_timing_repeat_bounds_period_start": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsPeriod.start",
                "type": "datetime",
            },
            "activity_detail_scheduled_timing_repeat_bounds_period_end": {
                "fhir_key": "detail.scheduledTiming.repeat.boundsPeriod.end",
                "type": "datetime",
            },
            # scheduledTiming.repeat
            "activity_detail_scheduled_timing_repeat_count": {
                "fhir_key": "detail.scheduledTiming.repeat.count",
                "type": "int",
            },
            "activity_detail_scheduled_timing_repeat_count_max": {
                "fhir_key": "detail.scheduledTiming.repeat.countMax",
                "type": "int",
            },
            "activity_detail_scheduled_timing_repeat_duration": {
                "fhir_key": "detail.scheduledTiming.repeat.duration",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_duration_max": {
                "fhir_key": "detail.scheduledTiming.repeat.durationMax",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_duration_unit": {
                "fhir_key": "detail.scheduledTiming.repeat.durationUnit",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_frequency": {
                "fhir_key": "detail.scheduledTiming.repeat.frequency",
                "type": "int",
            },
            "activity_detail_scheduled_timing_repeat_frequency_max": {
                "fhir_key": "detail.scheduledTiming.repeat.frequencyMax",
                "type": "int",
            },
            "activity_detail_scheduled_timing_repeat_period": {
                "fhir_key": "detail.scheduledTiming.repeat.duration",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_period_max": {
                "fhir_key": "detail.scheduledTiming.repeat.periodMax",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_period_unit": {
                "fhir_key": "detail.scheduledTiming.repeat.periodUnit",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_day_of_week": {
                "fhir_key": "detail.scheduledTiming.repeat.dayOfWeek",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_time_of_day": {
                "fhir_key": "detail.scheduledTiming.repeat.timeOfDay",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_when": {
                "fhir_key": "detail.scheduledTiming.repeat.when",
                "type": "str",
            },
            "activity_detail_scheduled_timing_repeat_offset": {
                "fhir_key": "detail.scheduledTiming.repeat.offset",
                "type": "str",
            },
            # scheduledPeriod
            "activity_detail_scheduled_period_start": {
                "fhir_key": "detail.scheduledPeriod.start",
                "type": "datetime",
            },
            "activity_detail_scheduled_period_end": {
                "fhir_key": "detail.scheduledPeriod.end",
                "type": "datetime",
            },
            # scheduledString
            "activity_detail_scheduled_string": {
                "fhir_key": "detail.scheduledString",
                "type": "str",
            },
            # end Scheduled element
            "activity_detail_location_reference": {
                "fhir_key": "detail.location.reference",
                "type": "str",
            },
            "activity_detail_location_type": {
                "fhir_key": "detail.location.type",
                "type": "str",
            },
            "activity_detail_location_display": {
                "fhir_key": "detail.location.display",
                "type": "str",
            },
            "activity_detail_performer": {
                "fhir_key": "detail.performer",
                "type": "str",
            },
            "activity_detail_product_codeable_concept_text": {
                "fhir_key": "detail.productCodeableConcept.text",
                "type": "str",
            },
            "activity_detail_product_codeable_concept_coding": {
                "fhir_key": "detail.productCodeableConcept.coding",
                "type": "str",
            },
            "activity_detail_product_reference_reference": {
                "fhir_key": "detail.productReference.reference",
                "type": "str",
            },
            "activity_detail_product_reference_display": {
                "fhir_key": "detail.productReference.display",
                "type": "str",
            },
            "activity_detail_product_reference_type": {
                "fhir_key": "detail.productReference.type",
                "type": "str",
            },
            "activity_detail_daily_amount_value": {
                "fhir_key": "detail.dailyAmount.value",
                "type": "str",
            },
            "activity_detail_daily_amount_unit": {
                "fhir_key": "detail.dailyAmount.unit",
                "type": "str",
            },
            "activity_detail_daily_amount_system": {
                "fhir_key": "detail.dailyAmount.system",
                "type": "str",
            },
            "activity_detail_daily_amount_code": {
                "fhir_key": "detail.dailyAmount.code",
                "type": "str",
            },
            "activity_detail_quantity_value": {
                "fhir_key": "detail.quantity.value",
                "type": "str",
            },
            "activity_detail_quantity_unit": {
                "fhir_key": "detail.quantity.unit",
                "type": "str",
            },
            "activity_detail_quantity_system": {
                "fhir_key": "detail.quantity.system",
                "type": "str",
            },
            "activity_detail_quantity_code": {
                "fhir_key": "detail.quantity.code",
                "type": "str",
            },
            "activity_detail_description": {
                "fhir_key": "detail.description",
                "type": "str",
            },
        },
    },
]


class CarePlanActivityTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'CarePlan' resource in FHIR, focusing on the 'activity' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'activity' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('activity').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanActivityTransformer instance with the resource type 'CarePlan',
            subtype 'activity', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "activity", TRANSFORM_SCHEMA)
