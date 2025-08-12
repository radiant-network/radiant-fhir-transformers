"""
FHIR Observation transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"},
        },
    },
    {
        "fhir_path": "status",
        "columns": {
            "status": {"fhir_key": "status", "type": "str"},
        },
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {"fhir_key": "reference", "type": "str"},
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {"fhir_key": "reference", "type": "str"},
            "encounter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "effectiveDateTime",
        "columns": {
            "effective_date_time": {
                "fhir_key": "effectiveDateTime",
                "type": "datetime",
            }
        },
    },
    {
        "fhir_path": "effectivePeriod",
        "columns": {
            "effective_period_start": {"fhir_key": "start", "type": "datetime"},
            "effective_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "effectiveTiming",
        "columns": {
            "effective_timing_repeat_bounds_duration_value": {
                "fhir_key": "repeat.boundsDuration.value",
                "type": "str",
            },
            "effective_timing_repeat_bounds_duration_comparator": {
                "fhir_key": "repeat.boundsDuration.comparator",
                "type": "str",
            },
            "effective_timing_repeat_bounds_duration_unit": {
                "fhir_key": "repeat.boundsDuration.unit",
                "type": "str",
            },
            "effective_timing_repeat_bounds_duration_system": {
                "fhir_key": "repeat.boundsDuration.system",
                "type": "str",
            },
            "effective_timing_repeat_bounds_duration_code": {
                "fhir_key": "repeat.boundsDuration.code",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_low_value": {
                "fhir_key": "repeat.boundsRange.low.value",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_low_unit": {
                "fhir_key": "repeat.boundsRange.low.unit",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_low_system": {
                "fhir_key": "repeat.boundsRange.low.system",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_low_code": {
                "fhir_key": "repeat.boundsRange.low.code",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_high_value": {
                "fhir_key": "repeat.boundsRange.high.value",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_high_unit": {
                "fhir_key": "repeat.boundsRange.high.unit",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_high_system": {
                "fhir_key": "repeat.boundsRange.high.system",
                "type": "str",
            },
            "effective_timing_repeat_bounds_range_high_code": {
                "fhir_key": "repeat.boundsRange.high.code",
                "type": "str",
            },
            "effective_timing_repeat_bounds_period_start": {
                "fhir_key": "repeat.boundsPeriod.start",
                "type": "datetime",
            },
            "effective_timing_repeat_bounds_period_end": {
                "fhir_key": "repeat.boundsPeriod.end",
                "type": "datetime",
            },
            "effective_timing_repeat_count": {
                "fhir_key": "repeat.count",
                "type": "int",
            },
            "effective_timing_repeat_count_max": {
                "fhir_key": "repeat.countMax",
                "type": "int",
            },
            "effective_timing_repeat_duration": {
                "fhir_key": "repeat.duration",
                "type": "str",
            },
            "effective_timing_repeat_duration_max": {
                "fhir_key": "repeat.durationMax",
                "type": "str",
            },
            "effective_timing_repeat_duration_unit": {
                "fhir_key": "repeat.durationUnit",
                "type": "str",
            },
            "effective_timing_repeat_frequency": {
                "fhir_key": "repeat.frequency",
                "type": "int",
            },
            "effective_timing_repeat_frequency_max": {
                "fhir_key": "repeat.frequencyMax",
                "type": "int",
            },
            "effective_timing_repeat_period": {
                "fhir_key": "repeat.period",
                "type": "str",
            },
            "effective_timing_repeat_period_max": {
                "fhir_key": "repeat.periodMax",
                "type": "str",
            },
            "effective_timing_repeat_period_unit": {
                "fhir_key": "repeat.periodUnit",
                "type": "str",
            },
            "effective_timing_repeat_offset": {
                "fhir_key": "repeat.offset",
                "type": "int",
            },
            "effective_timing_code_text": {
                "fhir_key": "code.text",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "effectiveInstant",
        "columns": {
            "effective_instant": {
                "fhir_key": "effectiveInstant",
                "type": "datetime",
            }
        },
    },
    {
        "fhir_path": "issued",
        "columns": {
            "issued": {"fhir_key": "issued", "type": "datetime"},
        },
    },
    {
        "fhir_path": "valueQuantity",
        "columns": {
            "value_quantity_value": {"fhir_key": "value", "type": "str"},
            "value_quantity_comparator": {
                "fhir_key": "comparator",
                "type": "str",
            },
            "value_quantity_unit": {"fhir_key": "unit", "type": "str"},
            "value_quantity_system": {"fhir_key": "system", "type": "str"},
            "value_quantity_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "valueCodeableConcept.text",
        "columns": {
            "value_codeable_concept_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "valueString",
        "columns": {
            "value_string": {"fhir_key": "valueString", "type": "str"},
        },
    },
    {
        "fhir_path": "valueBoolean",
        "columns": {
            "value_boolean": {"fhir_key": "valueBoolean", "type": "bool"},
        },
    },
    {
        "fhir_path": "valueInteger",
        "columns": {
            "value_integer": {"fhir_key": "valueInteger", "type": "int"},
        },
    },
    {
        "fhir_path": "valueRange",
        "columns": {
            "value_range_low_value": {"fhir_key": "low.value", "type": "str"},
            "value_range_low_unit": {"fhir_key": "low.unit", "type": "str"},
            "value_range_low_system": {"fhir_key": "low.system", "type": "str"},
            "value_range_low_code": {"fhir_key": "low.code", "type": "str"},
            "value_range_high_value": {"fhir_key": "high.value", "type": "str"},
            "value_range_high_unit": {"fhir_key": "high.unit", "type": "str"},
            "value_range_high_system": {
                "fhir_key": "high.system",
                "type": "str",
            },
            "value_range_high_code": {"fhir_key": "high.code", "type": "str"},
        },
    },
    {
        "fhir_path": "valueRatio",
        "columns": {
            "value_ratio_numerator_value": {
                "fhir_key": "numerator.value",
                "type": "str",
            },
            "value_ratio_numerator_comparator": {
                "fhir_key": "numerator.comparator",
                "type": "str",
            },
            "value_ratio_numerator_unit": {
                "fhir_key": "numerator.unit",
                "type": "str",
            },
            "value_ratio_numerator_system": {
                "fhir_key": "numerator.system",
                "type": "str",
            },
            "value_ratio_numerator_code": {
                "fhir_key": "numerator.code",
                "type": "str",
            },
            "value_ratio_denominator_value": {
                "fhir_key": "denominator.value",
                "type": "str",
            },
            "value_ratio_denominator_comparator": {
                "fhir_key": "denominator.comparator",
                "type": "str",
            },
            "value_ratio_denominator_unit": {
                "fhir_key": "denominator.unit",
                "type": "str",
            },
            "value_ratio_denominator_system": {
                "fhir_key": "denominator.system",
                "type": "str",
            },
            "value_ratio_denominator_code": {
                "fhir_key": "denominator.code",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "valueSampledData",
        "columns": {
            "value_sampled_data_origin_value": {
                "fhir_key": "origin.value",
                "type": "str",
            },
            "value_sampled_data_origin_unit": {
                "fhir_key": "origin.unit",
                "type": "str",
            },
            "value_sampled_data_origin_system": {
                "fhir_key": "origin.system",
                "type": "str",
            },
            "value_sampled_data_origin_code": {
                "fhir_key": "origin.code",
                "type": "str",
            },
            "value_sampled_data_period": {"fhir_key": "period", "type": "str"},
            "value_sampled_data_factor": {"fhir_key": "factor", "type": "str"},
            "value_sampled_data_lower_limit": {
                "fhir_key": "lowerLimit",
                "type": "str",
            },
            "value_sampled_data_upper_limit": {
                "fhir_key": "upperLimit",
                "type": "str",
            },
            "value_sampled_data_dimensions": {
                "fhir_key": "dimensions",
                "type": "int",
            },
            "value_sampled_data_data": {"fhir_key": "data", "type": "str"},
        },
    },
    {
        "fhir_path": "valueTime",
        "columns": {
            "value_time": {"fhir_key": "valueTime", "type": "str"},
        },
    },
    {
        "fhir_path": "valueDateTime",
        "columns": {
            "value_date_time": {
                "fhir_key": "valueDateTime",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "valuePeriod",
        "columns": {
            "value_period_start": {"fhir_key": "start", "type": "datetime"},
            "value_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "dataAbsentReason.text",
        "columns": {
            "data_absent_reason_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "bodySite.text",
        "columns": {
            "body_site_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "method.text",
        "columns": {
            "method_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "specimen",
        "fhir_reference": "specimen_reference",
        "columns": {
            "specimen_reference": {"fhir_key": "reference", "type": "str"},
            "specimen_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "device",
        "fhir_reference": "device_reference",
        "columns": {
            "device_reference": {"fhir_key": "reference", "type": "str"},
            "device_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ObservationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Observation' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file

    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ObservationTransformer instance with the resource
            type 'Observation' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", None, TRANSFORM_SCHEMA)
