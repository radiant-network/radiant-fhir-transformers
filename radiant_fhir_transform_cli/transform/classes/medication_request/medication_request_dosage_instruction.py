"""
FHIR MedicationRequest transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "columns": {
            "medication_request_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "dosageInstruction",
        "columns": {
            "dosage_instruction_text": {"fhir_key": "text", "type": "str"},
            "dosage_instruction_timing_code": {
                "fhir_key": "timing.code",
                "type": "str",
            },
            # Need an example of boundsDuration
            "dosage_instruction_timing_repeat_bounds_range_low_value": {
                "fhir_key": "boundsRange.low.value",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_bounds_range_low_unit": {
                "fhir_key": "boundsRange.low.unit",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_high_value": {
                "fhir_key": "boundsRange.high.value",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_bounds_range_high_unit": {
                "fhir_key": "boundsRange.high.unit",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_period_start": {
                "fhir_key": "timing.repeat.boundsPeriod.start",
                "type": "date",
            },
            "dosage_instruction_timing_repeat_bounds_period_end": {
                "fhir_key": "timing.repeat.boundsPeriod.end",
                "type": "date",
            },
            "dosage_instruction_timing_repeat_count": {
                "fhir_key": "timing.repeat.count",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_count_max": {
                "fhir_key": "timing.repeat.countMax",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_duration": {
                "fhir_key": "timing.repeat.duration",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_duration_max": {
                "fhir_key": "timing.repeat.durationMax",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_duration_unit": {
                "fhir_key": "timing.repeat.durationUnit",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_frequency": {
                "fhir_key": "timing.repeat.frequency",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_frequency_max": {
                "fhir_key": "timing.repeat.frequencyMax",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_period": {
                "fhir_key": "timing.repeat.period",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_period_max": {
                "fhir_key": "timing.repeat.periodMax",
                "type": "int",
            },
            "dosage_instruction_timing_repeat_period_unit": {
                "fhir_key": "timing.repeat.periodUnit",
                "type": "str",
            },
        },
    },
]


class MedicationRequestCategoryCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Medication' resource in FHIR.

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
        super().__init__(
            "MedicationRequest", "category_coding", TRANSFORM_SCHEMA
        )
