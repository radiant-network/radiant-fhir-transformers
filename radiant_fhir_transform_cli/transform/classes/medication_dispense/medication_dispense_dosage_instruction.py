""""
FHIR MedicationDispense DosageInstruction transformer
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
            "medication_dispense_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "dosageInstruction",
        "columns": {
            "dosage_instruction_sequence": {
                "fhir_key": "sequence",
                "type": "int",
            },
            "dosage_instruction_text": {"fhir_key": "text", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_additional_instruction_coding": {
            #     "fhir_key": "additionalInstruction.coding",
            #     "type": "str",
            # },
            # "dosage_instruction_additional_instruction_text": {
            #     "fhir_key": "additionalInstruction.text",
            #     "type": "str",
            # },
            "dosage_instruction_patient_instruction": {
                "fhir_key": "patientInstruction",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_timing_event": {
            #     "fhir_key": "timing.event",
            #     "type": "datetime",
            # },
            "dosage_instruction_timing_repeat_bounds_duration_value": {
                "fhir_key": "timing.repeat.boundsDuration.value",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_duration_unit": {
                "fhir_key": "timing.repeat.boundsDuration.unit",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_duration_system": {
                "fhir_key": "timing.repeat.boundsDuration.system",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_duration_code": {
                "fhir_key": "timing.repeat.boundsDuration.code",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_low_value": {
                "fhir_key": "timing.repeat.boundsRange.low.value",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_low_unit": {
                "fhir_key": "timing.repeat.boundsRange.low.unit",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_low_system": {
                "fhir_key": "timing.repeat.boundsRange.low.system",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_low_code": {
                "fhir_key": "timing.repeat.boundsRange.low.code",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_high_value": {
                "fhir_key": "timing.repeat.boundsRange.high.value",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_high_unit": {
                "fhir_key": "timing.repeat.boundsRange.high.unit",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_high_system": {
                "fhir_key": "timing.repeat.boundsRange.high.system",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_range_high_code": {
                "fhir_key": "timing.repeat.boundsRange.high.code",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_period_start": {
                "fhir_key": "timing.repeat.boundsPeriod.start",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_bounds_period_end": {
                "fhir_key": "timing.repeat.boundsPeriod.end",
                "type": "str",
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
                "type": "str",
            },
            "dosage_instruction_timing_repeat_duration_max": {
                "fhir_key": "timing.repeat.durationMax",
                "type": "str",
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
                "type": "str",
            },
            "dosage_instruction_timing_repeat_period_max": {
                "fhir_key": "timing.repeat.periodMax",
                "type": "str",
            },
            "dosage_instruction_timing_repeat_period_unit": {
                "fhir_key": "timing.repeat.periodUnit",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_timing_repeat_day_of_week": {
            #     "fhir_key": "timing.repeat.dayOfWeek",
            #     "type": "str",
            # },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_timing_repeat_time_of_day": {
            #     "fhir_key": "timing.repeat.timeOfDay",
            #     "type": "str",
            # },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_timing_repeat_when": {
            #     "fhir_key": "timing.repeat.when",
            #     "type": "str",
            # },
            "dosage_instruction_timing_repeat_offset": {
                "fhir_key": "timing.repeat.offset",
                "type": "int",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_timing_code_coding": {
            #     "fhir_key": "timing.code.coding",
            #     "type": "str",
            # },
            "dosage_instruction_timing_code_text": {
                "fhir_key": "timing.code.text",
                "type": "str",
            },
            "dosage_instruction_as_needed_boolean": {
                "fhir_key": "asNeededBoolean",
                "type": "bool",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_as_needed_codeable_concept_coding": {
            #     "fhir_key": "asNeededCodeableConcept.coding",
            #     "type": "str",
            # },
            "dosage_instruction_as_needed_codeable_concept_text": {
                "fhir_key": "asNeededCodeableConcept.text",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_site_coding": {
            #     "fhir_key": "site.coding",
            #     "type": "str",
            # },
            "dosage_instruction_site_text": {
                "fhir_key": "site.text",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_route_coding": {
            #     "fhir_key": "route.coding",
            #     "type": "str",
            # },
            "dosage_instruction_route_text": {
                "fhir_key": "route.text",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_method_coding": {
            #     "fhir_key": "method.coding",
            #     "type": "str",
            # },
            "dosage_instruction_method_text": {
                "fhir_key": "method.text",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            # "dosage_instruction_dose_and_rate_type_coding": {
            #     "fhir_key": "doseAndRate.coding",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_type_text": {
            #     "fhir_key": "doseAndRate.text",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_low_value": {
            #     "fhir_key": "doseAndRate.doseRange.low.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_low_unit": {
            #     "fhir_key": "doseAndRate.doseRange.low.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_low_system": {
            #     "fhir_key": "doseAndRate.doseRange.low.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_low_code": {
            #     "fhir_key": "doseAndRate.doseRange.low.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_high_value": {
            #     "fhir_key": "doseAndRate.doseRange.high.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_high_unit": {
            #     "fhir_key": "doseAndRate.doseRange.high.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_high_system": {
            #     "fhir_key": "doseAndRate.doseRange.high.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_range_high_code": {
            #     "fhir_key": "doseAndRate.doseRange.high.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_quantity_value": {
            #     "fhir_key": "doseAndRate.doseQuantity.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_quantity_unit": {
            #     "fhir_key": "doseAndRate.doseQuantity.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_quantity_system": {
            #     "fhir_key": "doseAndRate.doseQuantity.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_dose_quantity_code": {
            #     "fhir_key": "doseAndRate.doseQuantity.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_numerator_value": {
            #     "fhir_key": "doseAndRate.rateRatio.numerator.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_numerator_unit": {
            #     "fhir_key": "doseAndRate.rateRatio.numerator.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_numerator_system": {
            #     "fhir_key": "doseAndRate.rateRatio.numerator.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_numerator_code": {
            #     "fhir_key": "doseAndRate.rateRatio.numerator.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_denominator_value": {
            #     "fhir_key": "doseAndRate.rateRatio.denominator.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_denominator_unit": {
            #     "fhir_key": "doseAndRate.rateRatio.denominator.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_denominator_system": {
            #     "fhir_key": "doseAndRate.rateRatio.denominator.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_ratio_denominator_code": {
            #     "fhir_key": "doseAndRate.rateRatio.denominator.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_low_value": {
            #     "fhir_key": "doseAndRate.rateRange.low.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_low_unit": {
            #     "fhir_key": "doseAndRate.rateRange.low.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_low_system": {
            #     "fhir_key": "doseAndRate.rateRange.low.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_low_code": {
            #     "fhir_key": "doseAndRate.rateRange.low.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_high_value": {
            #     "fhir_key": "doseAndRate.rateRange.high.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_high_unit": {
            #     "fhir_key": "doseAndRate.rateRange.high.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_high_system": {
            #     "fhir_key": "doseAndRate.rateRange.high.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_range_high_code": {
            #     "fhir_key": "doseAndRate.rateRange.high.code",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_quantity_value": {
            #     "fhir_key": "doseAndRate.rateQuantity.value",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_quantity_unit": {
            #     "fhir_key": "doseAndRate.rateQuantity.unit",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_quantity_system": {
            #     "fhir_key": "doseAndRate.rateQuantity.system",
            #     "type": "str",
            # },
            # "dosage_instruction_dose_and_rate_rate_quantity_code": {
            #     "fhir_key": "doseAndRate.rateQuantity.code",
            #     "type": "str",
            # },
            "dosage_instruction_max_dose_per_period_numerator_value": {
                "fhir_key": "maxDosePerPeriod.numerator.value",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_numerator_unit": {
                "fhir_key": "maxDosePerPeriod.numerator.unit",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_numerator_system": {
                "fhir_key": "maxDosePerPeriod.numerator.system",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_numerator_code": {
                "fhir_key": "maxDosePerPeriod.numerator.code",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_denominator_value": {
                "fhir_key": "maxDosePerPeriod.denominator.value",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_denominator_unit": {
                "fhir_key": "maxDosePerPeriod.denominator.unit",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_denominator_system": {
                "fhir_key": "maxDosePerPeriod.denominator.system",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_period_denominator_code": {
                "fhir_key": "maxDosePerPeriod.denominator.code",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_administration_value": {
                "fhir_key": "maxDosePerAdministration.value",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_administration_unit": {
                "fhir_key": "maxDosePerAdministration.unit",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_administration_system": {
                "fhir_key": "maxDosePerAdministration.system",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_administration_code": {
                "fhir_key": "maxDosePerAdministration.code",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_lifetime_value": {
                "fhir_key": "maxDosePerLifetime.value",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_lifetime_unit": {
                "fhir_key": "maxDosePerLifetime.unit",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_lifetime_system": {
                "fhir_key": "maxDosePerLifetime.system",
                "type": "str",
            },
            "dosage_instruction_max_dose_per_lifetime_code": {
                "fhir_key": "maxDosePerLifetime.code",
                "type": "str",
            },
        },
    },
]


class MedicationDispenseDosageInstructionTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR, focusing on the 'dosageInstruction' element.

    This class transforms FHIR MedicationDispense JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'dosageInstruction' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('MedicationDispense').
        subtype (str): Specifies the sub-element of the resource to focus on ('dosage_instruction').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the MedicationDispenseDosageInstructionTransformer instance with the resource type 'MedicationDispense',
            subtype 'dosage_instruction', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "MedicationDispense", "dosage_instruction", TRANSFORM_SCHEMA
        )
