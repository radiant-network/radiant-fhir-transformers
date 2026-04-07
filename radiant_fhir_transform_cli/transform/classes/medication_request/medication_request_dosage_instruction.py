"""FHIR MedicationRequest dosage_instruction transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request_dosage_instruction",
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
                    "name": "medication_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "dosageInstruction",
            "column": [
                {
                    "name": "dosage_instruction_sequence",
                    "path": "sequence",
                    "type": "integer",
                },
                {
                    "name": "dosage_instruction_text",
                    "path": "text",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_patient_instruction",
                    "path": "patientInstruction",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_duration_value",
                    "path": "timing.repeat.boundsDuration.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_duration_unit",
                    "path": "timing.repeat.boundsDuration.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_duration_system",
                    "path": "timing.repeat.boundsDuration.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_duration_code",
                    "path": "timing.repeat.boundsDuration.code",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_low_value",
                    "path": "timing.repeat.boundsRange.low.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_low_unit",
                    "path": "timing.repeat.boundsRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_low_system",
                    "path": "timing.repeat.boundsRange.low.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_low_code",
                    "path": "timing.repeat.boundsRange.low.code",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_high_value",
                    "path": "timing.repeat.boundsRange.high.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_high_unit",
                    "path": "timing.repeat.boundsRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_high_system",
                    "path": "timing.repeat.boundsRange.high.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_range_high_code",
                    "path": "timing.repeat.boundsRange.high.code",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_period_start",
                    "path": "timing.repeat.boundsPeriod.start",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_bounds_period_end",
                    "path": "timing.repeat.boundsPeriod.end",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_count",
                    "path": "timing.repeat.count",
                    "type": "integer",
                },
                {
                    "name": "dosage_instruction_timing_repeat_count_max",
                    "path": "timing.repeat.countMax",
                    "type": "integer",
                },
                {
                    "name": "dosage_instruction_timing_repeat_duration",
                    "path": "timing.repeat.duration",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_duration_max",
                    "path": "timing.repeat.durationMax",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_duration_unit",
                    "path": "timing.repeat.durationUnit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_frequency",
                    "path": "timing.repeat.frequency",
                    "type": "integer",
                },
                {
                    "name": "dosage_instruction_timing_repeat_frequency_max",
                    "path": "timing.repeat.frequencyMax",
                    "type": "integer",
                },
                {
                    "name": "dosage_instruction_timing_repeat_period",
                    "path": "timing.repeat.period",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_period_max",
                    "path": "timing.repeat.periodMax",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_period_unit",
                    "path": "timing.repeat.periodUnit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_timing_repeat_offset",
                    "path": "timing.repeat.offset",
                    "type": "integer",
                },
                {
                    "name": "dosage_instruction_timing_code_text",
                    "path": "timing.code.text",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_as_needed_boolean",
                    "path": "asNeededBoolean",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_as_needed_codeable_concept_text",
                    "path": "asNeededCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_site_text",
                    "path": "site.text",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_route_text",
                    "path": "route.text",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_method_text",
                    "path": "method.text",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_numerator_value",
                    "path": "maxDosePerPeriod.numerator.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_numerator_unit",
                    "path": "maxDosePerPeriod.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_numerator_system",
                    "path": "maxDosePerPeriod.numerator.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_numerator_code",
                    "path": "maxDosePerPeriod.numerator.code",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_denominator_value",
                    "path": "maxDosePerPeriod.denominator.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_denominator_unit",
                    "path": "maxDosePerPeriod.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_denominator_system",
                    "path": "maxDosePerPeriod.denominator.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_period_denominator_code",
                    "path": "maxDosePerPeriod.denominator.code",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_administration_value",
                    "path": "maxDosePerAdministration.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_administration_unit",
                    "path": "maxDosePerAdministration.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_administration_system",
                    "path": "maxDosePerAdministration.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_administration_code",
                    "path": "maxDosePerAdministration.code",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_lifetime_value",
                    "path": "maxDosePerLifetime.value",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_lifetime_unit",
                    "path": "maxDosePerLifetime.unit",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_lifetime_system",
                    "path": "maxDosePerLifetime.system",
                    "type": "string",
                },
                {
                    "name": "dosage_instruction_max_dose_per_lifetime_code",
                    "path": "maxDosePerLifetime.code",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "additionalInstruction",
                    "column": [
                        {
                            "name": "dosage_instruction_additional_instruction_text",
                            "path": "text",
                            "type": "string",
                        },
                    ],
                    "select": [
                        {
                            "forEachOrNull": "coding",
                            "column": [
                                {
                                    "name": "dosage_instruction_additional_instruction_coding_system",
                                    "path": "system",
                                    "type": "string",
                                },
                                {
                                    "name": "dosage_instruction_additional_instruction_coding_code",
                                    "path": "code",
                                    "type": "string",
                                },
                                {
                                    "name": "dosage_instruction_additional_instruction_coding_display",
                                    "path": "display",
                                    "type": "string",
                                },
                            ],
                        },
                    ],
                },
                {
                    "forEachOrNull": "timing.event",
                    "column": [
                        {
                            "name": "dosage_instruction_timing_event",
                            "path": "$this",
                            "type": "datetime",
                        },
                    ],
                },
                {
                    "forEachOrNull": "timing.repeat.dayOfWeek",
                    "column": [
                        {
                            "name": "dosage_instruction_timing_repeat_day_of_week",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "timing.repeat.timeOfDay",
                    "column": [
                        {
                            "name": "dosage_instruction_timing_repeat_time_of_day",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "timing.repeat.when",
                    "column": [
                        {
                            "name": "dosage_instruction_timing_repeat_when",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "timing.code.coding",
                    "column": [
                        {
                            "name": "dosage_instruction_timing_code_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_timing_code_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_timing_code_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "asNeededCodeableConcept.coding",
                    "column": [
                        {
                            "name": "dosage_instruction_as_needed_codeable_concept_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_as_needed_codeable_concept_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_as_needed_codeable_concept_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "site.coding",
                    "column": [
                        {
                            "name": "dosage_instruction_site_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_site_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_site_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "route.coding",
                    "column": [
                        {
                            "name": "dosage_instruction_route_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_route_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_route_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "method.coding",
                    "column": [
                        {
                            "name": "dosage_instruction_method_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_method_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_method_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "doseAndRate",
                    "column": [
                        {
                            "name": "dosage_instruction_dose_and_rate_type_text",
                            "path": "type.text",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_low_value",
                            "path": "doseRange.low.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_low_unit",
                            "path": "doseRange.low.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_low_system",
                            "path": "doseRange.low.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_low_code",
                            "path": "doseRange.low.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_high_value",
                            "path": "doseRange.high.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_high_unit",
                            "path": "doseRange.high.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_high_system",
                            "path": "doseRange.high.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_range_high_code",
                            "path": "doseRange.high.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_quantity_value",
                            "path": "doseQuantity.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_quantity_unit",
                            "path": "doseQuantity.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_quantity_system",
                            "path": "doseQuantity.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_dose_quantity_code",
                            "path": "doseQuantity.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_numerator_value",
                            "path": "rateRatio.numerator.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_numerator_unit",
                            "path": "rateRatio.numerator.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_numerator_system",
                            "path": "rateRatio.numerator.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_numerator_code",
                            "path": "rateRatio.numerator.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_denominator_value",
                            "path": "rateRatio.denominator.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_denominator_unit",
                            "path": "rateRatio.denominator.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_denominator_system",
                            "path": "rateRatio.denominator.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_ratio_denominator_code",
                            "path": "rateRatio.denominator.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_low_value",
                            "path": "rateRange.low.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_low_unit",
                            "path": "rateRange.low.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_low_system",
                            "path": "rateRange.low.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_low_code",
                            "path": "rateRange.low.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_high_value",
                            "path": "rateRange.high.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_high_unit",
                            "path": "rateRange.high.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_high_system",
                            "path": "rateRange.high.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_range_high_code",
                            "path": "rateRange.high.code",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_quantity_value",
                            "path": "rateQuantity.value",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_quantity_unit",
                            "path": "rateQuantity.unit",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_quantity_system",
                            "path": "rateQuantity.system",
                            "type": "string",
                        },
                        {
                            "name": "dosage_instruction_dose_and_rate_rate_quantity_code",
                            "path": "rateQuantity.code",
                            "type": "string",
                        },
                    ],
                    "select": [
                        {
                            "forEachOrNull": "type.coding",
                            "column": [
                                {
                                    "name": "dosage_instruction_dose_and_rate_type_coding_system",
                                    "path": "system",
                                    "type": "string",
                                },
                                {
                                    "name": "dosage_instruction_dose_and_rate_type_coding_code",
                                    "path": "code",
                                    "type": "string",
                                },
                                {
                                    "name": "dosage_instruction_dose_and_rate_type_coding_display",
                                    "path": "display",
                                    "type": "string",
                                },
                            ],
                        },
                    ],
                },
            ],
        },
    ],
}


class MedicationRequestDosageInstructionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationRequest", "dosage_instruction", VIEW_DEFINITION)
