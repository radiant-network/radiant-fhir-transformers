"""FHIR RequestGroup action transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "RequestGroup",
    "name": "request_group_action",
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
                    "name": "request_group_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "action",
            "column": [
                {
                    "name": "action_prefix",
                    "path": "prefix",
                    "type": "string",
                },
                {
                    "name": "action_title",
                    "path": "title",
                    "type": "string",
                },
                {
                    "name": "action_description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "action_text_equivalent",
                    "path": "textEquivalent",
                    "type": "string",
                },
                {
                    "name": "action_priority",
                    "path": "priority",
                    "type": "string",
                },
                {
                    "name": "action_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "action_documentation",
                    "path": "documentation",
                    "type": "string",
                },
                {
                    "name": "action_condition",
                    "path": "condition",
                    "type": "string",
                },
                {
                    "name": "action_related_action",
                    "path": "relatedAction",
                    "type": "string",
                },
                {
                    "name": "action_timing_date_time",
                    "path": "timingDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "action_timing_age_value",
                    "path": "timingAge.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_age_comparator",
                    "path": "timingAge.comparator",
                    "type": "string",
                },
                {
                    "name": "action_timing_age_unit",
                    "path": "timingAge.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_age_system",
                    "path": "timingAge.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_age_code",
                    "path": "timingAge.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_period_start",
                    "path": "timingPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "action_timing_period_end",
                    "path": "timingPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "action_timing_duration_value",
                    "path": "timingDuration.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_duration_comparator",
                    "path": "timingDuration.comparator",
                    "type": "string",
                },
                {
                    "name": "action_timing_duration_unit",
                    "path": "timingDuration.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_duration_system",
                    "path": "timingDuration.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_duration_code",
                    "path": "timingDuration.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_low_value",
                    "path": "timingRange.low.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_low_unit",
                    "path": "timingRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_low_system",
                    "path": "timingRange.low.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_low_code",
                    "path": "timingRange.low.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_high_value",
                    "path": "timingRange.high.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_high_unit",
                    "path": "timingRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_high_system",
                    "path": "timingRange.high.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_range_high_code",
                    "path": "timingRange.high.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_event",
                    "path": "timingTiming.event",
                    "type": "dateTime",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_duration_value",
                    "path": "timingTiming.repeat.boundsDuration.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_duration_comparator",
                    "path": "timingTiming.repeat.boundsDuration.comparator",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_duration_unit",
                    "path": "timingTiming.repeat.boundsDuration.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_duration_system",
                    "path": "timingTiming.repeat.boundsDuration.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_duration_code",
                    "path": "timingTiming.repeat.boundsDuration.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_low_value",
                    "path": "timingTiming.repeat.boundsRange.low.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_low_unit",
                    "path": "timingTiming.repeat.boundsRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_low_system",
                    "path": "timingTiming.repeat.boundsRange.low.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_low_code",
                    "path": "timingTiming.repeat.boundsRange.low.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_high_value",
                    "path": "timingTiming.repeat.boundsRange.high.value",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_high_unit",
                    "path": "timingTiming.repeat.boundsRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_high_system",
                    "path": "timingTiming.repeat.boundsRange.high.system",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_range_high_code",
                    "path": "timingTiming.repeat.boundsRange.high.code",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_period_start",
                    "path": "timingTiming.repeat.boundsPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "action_timing_timing_repeat_bounds_period_end",
                    "path": "timingTiming.repeat.boundsPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "action_timing_timing_repeat_count",
                    "path": "timingTiming.repeat.count",
                    "type": "integer",
                },
                {
                    "name": "action_timing_timing_repeat_count_max",
                    "path": "timingTiming.repeat.countMax",
                    "type": "integer",
                },
                {
                    "name": "action_timing_timing_repeat_duration",
                    "path": "timingTiming.repeat.duration",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_duration_max",
                    "path": "timingTiming.repeat.durationMax",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_duration_unit",
                    "path": "timingTiming.repeat.durationUnit",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_frequency",
                    "path": "timingTiming.repeat.frequency",
                    "type": "integer",
                },
                {
                    "name": "action_timing_timing_repeat_frequency_max",
                    "path": "timingTiming.repeat.frequencyMax",
                    "type": "integer",
                },
                {
                    "name": "action_timing_timing_repeat_period",
                    "path": "timingTiming.repeat.period",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_period_max",
                    "path": "timingTiming.repeat.periodMax",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_period_unit",
                    "path": "timingTiming.repeat.periodUnit",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_day_of_week",
                    "path": "timingTiming.repeat.dayOfWeek",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_time_of_day",
                    "path": "timingTiming.repeat.timeOfDay",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_when",
                    "path": "timingTiming.repeat.when",
                    "type": "string",
                },
                {
                    "name": "action_timing_timing_repeat_offset",
                    "path": "timingTiming.repeat.offset",
                    "type": "integer",
                },
                {
                    "name": "action_timing_timing_code",
                    "path": "timingTiming.code",
                    "type": "string",
                },
                {
                    "name": "action_type_coding",
                    "path": "type.coding",
                    "type": "string",
                },
                {
                    "name": "action_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "action_grouping_behavior",
                    "path": "groupingBehavior",
                    "type": "string",
                },
                {
                    "name": "action_selection_behavior",
                    "path": "selectionBehavior",
                    "type": "string",
                },
                {
                    "name": "action_required_behavior",
                    "path": "requiredBehavior",
                    "type": "string",
                },
                {
                    "name": "action_precheck_behavior",
                    "path": "precheckBehavior",
                    "type": "string",
                },
                {
                    "name": "action_cardinality_behavior",
                    "path": "cardinalityBehavior",
                    "type": "string",
                },
                {
                    "name": "action_resource_reference",
                    "path": "resource.reference",
                    "type": "string",
                },
                {
                    "name": "action_resource_type",
                    "path": "resource.type",
                    "type": "string",
                },
                {
                    "name": "action_resource_display",
                    "path": "resource.display",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "participant",
                    "column": [
                        {
                            "name": "action_participant",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "action",
                    "column": [
                        {
                            "name": "action_action",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class RequestGroupActionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("RequestGroup", "action", VIEW_DEFINITION)
