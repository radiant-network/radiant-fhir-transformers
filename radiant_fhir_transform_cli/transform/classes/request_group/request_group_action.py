"""
FHIR RequestGroup Action transformer
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
            "request_group_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "action",
        "columns": {
            "action_prefix": {"fhir_key": "prefix", "type": "str"},
            "action_title": {"fhir_key": "title", "type": "str"},
            "action_description": {"fhir_key": "description", "type": "str"},
            "action_text_equivalent": {
                "fhir_key": "textEquivalent",
                "type": "str",
            },
            "action_priority": {"fhir_key": "priority", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_code": {"fhir_key": "code", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_documentation": {
                "fhir_key": "documentation",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_condition": {"fhir_key": "condition", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_related_action": {
                "fhir_key": "relatedAction",
                "type": "str",
            },
            "action_timing_date_time": {
                "fhir_key": "timingDateTime",
                "type": "datetime",
            },
            "action_timing_age_value": {
                "fhir_key": "timingAge.value",
                "type": "str",
            },
            "action_timing_age_comparator": {
                "fhir_key": "timingAge.comparator",
                "type": "str",
            },
            "action_timing_age_unit": {
                "fhir_key": "timingAge.unit",
                "type": "str",
            },
            "action_timing_age_system": {
                "fhir_key": "timingAge.system",
                "type": "str",
            },
            "action_timing_age_code": {
                "fhir_key": "timingAge.code",
                "type": "str",
            },
            "action_timing_period_start": {
                "fhir_key": "timingPeriod.start",
                "type": "datetime",
            },
            "action_timing_period_end": {
                "fhir_key": "timingPeriod.end",
                "type": "datetime",
            },
            "action_timing_duration_value": {
                "fhir_key": "timingDuration.value",
                "type": "str",
            },
            "action_timing_duration_comparator": {
                "fhir_key": "timingDuration.comparator",
                "type": "str",
            },
            "action_timing_duration_unit": {
                "fhir_key": "timingDuration.unit",
                "type": "str",
            },
            "action_timing_duration_system": {
                "fhir_key": "timingDuration.system",
                "type": "str",
            },
            "action_timing_duration_code": {
                "fhir_key": "timingDuration.code",
                "type": "str",
            },
            "action_timing_range_low_value": {
                "fhir_key": "timingRange.low.value",
                "type": "str",
            },
            "action_timing_range_low_unit": {
                "fhir_key": "timingRange.low.unit",
                "type": "str",
            },
            "action_timing_range_low_system": {
                "fhir_key": "timingRange.low.system",
                "type": "str",
            },
            "action_timing_range_low_code": {
                "fhir_key": "timingRange.low.code",
                "type": "str",
            },
            "action_timing_range_high_value": {
                "fhir_key": "timingRange.high.value",
                "type": "str",
            },
            "action_timing_range_high_unit": {
                "fhir_key": "timingRange.high.unit",
                "type": "str",
            },
            "action_timing_range_high_system": {
                "fhir_key": "timingRange.high.system",
                "type": "str",
            },
            "action_timing_range_high_code": {
                "fhir_key": "timingRange.high.code",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_timing_timing_event": {
                "fhir_key": "timingTiming.event",
                "type": "datetime",
            },
            "action_timing_timing_repeat_bounds_duration_value": {
                "fhir_key": "timingTiming.repeat.boundsDuration.value",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_duration_comparator": {
                "fhir_key": "timingTiming.repeat.boundsDuration.comparator",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_duration_unit": {
                "fhir_key": "timingTiming.repeat.boundsDuration.unit",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_duration_system": {
                "fhir_key": "timingTiming.repeat.boundsDuration.system",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_duration_code": {
                "fhir_key": "timingTiming.repeat.boundsDuration.code",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_low_value": {
                "fhir_key": "timingTiming.repeat.boundsRange.low.value",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_low_unit": {
                "fhir_key": "timingTiming.repeat.boundsRange.low.unit",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_low_system": {
                "fhir_key": "timingTiming.repeat.boundsRange.low.system",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_low_code": {
                "fhir_key": "timingTiming.repeat.boundsRange.low.code",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_high_value": {
                "fhir_key": "timingTiming.repeat.boundsRange.high.value",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_high_unit": {
                "fhir_key": "timingTiming.repeat.boundsRange.high.unit",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_high_system": {
                "fhir_key": "timingTiming.repeat.boundsRange.high.system",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_range_high_code": {
                "fhir_key": "timingTiming.repeat.boundsRange.high.code",
                "type": "str",
            },
            "action_timing_timing_repeat_bounds_period_start": {
                "fhir_key": "timingTiming.repeat.boundsPeriod.start",
                "type": "datetime",
            },
            "action_timing_timing_repeat_bounds_period_end": {
                "fhir_key": "timingTiming.repeat.boundsPeriod.end",
                "type": "datetime",
            },
            "action_timing_timing_repeat_count": {
                "fhir_key": "timingTiming.repeat.count",
                "type": "int",
            },
            "action_timing_timing_repeat_count_max": {
                "fhir_key": "timingTiming.repeat.countMax",
                "type": "int",
            },
            "action_timing_timing_repeat_duration": {
                "fhir_key": "timingTiming.repeat.duration",
                "type": "str",
            },
            "action_timing_timing_repeat_duration_max": {
                "fhir_key": "timingTiming.repeat.durationMax",
                "type": "str",
            },
            "action_timing_timing_repeat_duration_unit": {
                "fhir_key": "timingTiming.repeat.durationUnit",
                "type": "str",
            },
            "action_timing_timing_repeat_frequency": {
                "fhir_key": "timingTiming.repeat.frequency",
                "type": "int",
            },
            "action_timing_timing_repeat_frequency_max": {
                "fhir_key": "timingTiming.repeat.frequencyMax",
                "type": "int",
            },
            "action_timing_timing_repeat_period": {
                "fhir_key": "timingTiming.repeat.period",
                "type": "str",
            },
            "action_timing_timing_repeat_period_max": {
                "fhir_key": "timingTiming.repeat.periodMax",
                "type": "str",
            },
            "action_timing_timing_repeat_period_unit": {
                "fhir_key": "timingTiming.repeat.periodUnit",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_timing_timing_repeat_day_of_week": {
                "fhir_key": "timingTiming.repeat.dayOfWeek",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_timing_timing_repeat_time_of_day": {
                "fhir_key": "timingTiming.repeat.timeOfDay",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_timing_timing_repeat_when": {
                "fhir_key": "timingTiming.repeat.when",
                "type": "str",
            },
            "action_timing_timing_repeat_offset": {
                "fhir_key": "timingTiming.repeat.offset",
                "type": "int",
            },
            "action_timing_timing_code": {
                "fhir_key": "timingTiming.code",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_participant": {"fhir_key": "participant", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "action_type_coding": {"fhir_key": "type.coding", "type": "str"},
            "action_type_text": {"fhir_key": "type.text", "type": "str"},
            "action_grouping_behavior": {
                "fhir_key": "groupingBehavior",
                "type": "str",
            },
            "action_selection_behavior": {
                "fhir_key": "selectionBehavior",
                "type": "str",
            },
            "action_required_behavior": {
                "fhir_key": "requiredBehavior",
                "type": "str",
            },
            "action_precheck_behavior": {
                "fhir_key": "precheckBehavior",
                "type": "str",
            },
            "action_cardinality_behavior": {
                "fhir_key": "cardinalityBehavior",
                "type": "str",
            },
            "action_resource_reference": {
                "fhir_key": "resource.reference",
                "type": "str",
            },
            "action_resource_type": {
                "fhir_key": "resource.type",
                "type": "str",
            },
            "action_resource_display": {
                "fhir_key": "resource.display",
                "type": "str",
            },
            "action_action": {"fhir_key": "action", "type": "str"},
        },
    },
]


class RequestGroupActionTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RequestGroup' resource in FHIR, focusing on the 'action' element.

    This class transforms FHIR RequestGroup JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'action' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RequestGroup').
        subtype (str): Specifies the sub-element of the resource to focus on ('action').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RequestGroupActionTransformer instance with the resource type 'RequestGroup',
            subtype 'action', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RequestGroup", "action", TRANSFORM_SCHEMA)
