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
        },
    ],
}


class MedicationRequestDosageInstructionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__(
            "MedicationRequest", "dosage_instruction", VIEW_DEFINITION
        )
