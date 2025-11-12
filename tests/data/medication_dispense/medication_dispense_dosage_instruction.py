"""
Test helper class for FHIR resource type MedicationDispense dosageInstruction
"""

from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseDosageInstructionTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_dispense_id": "meddisp001",
        "dosage_instruction_sequence": 1,
        "dosage_instruction_text": "500mg IV q6h x 3 days",
        "dosage_instruction_patient_instruction": None,
        "dosage_instruction_timing_repeat_bounds_duration_value": None,
        "dosage_instruction_timing_repeat_bounds_duration_unit": None,
        "dosage_instruction_timing_repeat_bounds_duration_system": None,
        "dosage_instruction_timing_repeat_bounds_duration_code": None,
        "dosage_instruction_timing_repeat_bounds_range_low_value": None,
        "dosage_instruction_timing_repeat_bounds_range_low_unit": None,
        "dosage_instruction_timing_repeat_bounds_range_low_system": None,
        "dosage_instruction_timing_repeat_bounds_range_low_code": None,
        "dosage_instruction_timing_repeat_bounds_range_high_value": None,
        "dosage_instruction_timing_repeat_bounds_range_high_unit": None,
        "dosage_instruction_timing_repeat_bounds_range_high_system": None,
        "dosage_instruction_timing_repeat_bounds_range_high_code": None,
        "dosage_instruction_timing_repeat_bounds_period_start": None,
        "dosage_instruction_timing_repeat_bounds_period_end": None,
        "dosage_instruction_timing_repeat_count": None,
        "dosage_instruction_timing_repeat_count_max": None,
        "dosage_instruction_timing_repeat_duration": None,
        "dosage_instruction_timing_repeat_duration_max": None,
        "dosage_instruction_timing_repeat_duration_unit": None,
        "dosage_instruction_timing_repeat_frequency": 1,
        "dosage_instruction_timing_repeat_frequency_max": None,
        "dosage_instruction_timing_repeat_period": 6,
        "dosage_instruction_timing_repeat_period_max": None,
        "dosage_instruction_timing_repeat_period_unit": "h",
        "dosage_instruction_timing_repeat_offset": None,
        "dosage_instruction_timing_code_text": None,
        "dosage_instruction_as_needed_boolean": None,
        "dosage_instruction_as_needed_codeable_concept_text": None,
        "dosage_instruction_site_text": None,
        "dosage_instruction_route_text": None,
        "dosage_instruction_method_text": None,
        "dosage_instruction_max_dose_per_period_numerator_value": None,
        "dosage_instruction_max_dose_per_period_numerator_unit": None,
        "dosage_instruction_max_dose_per_period_numerator_system": None,
        "dosage_instruction_max_dose_per_period_numerator_code": None,
        "dosage_instruction_max_dose_per_period_denominator_value": None,
        "dosage_instruction_max_dose_per_period_denominator_unit": None,
        "dosage_instruction_max_dose_per_period_denominator_system": None,
        "dosage_instruction_max_dose_per_period_denominator_code": None,
        "dosage_instruction_max_dose_per_administration_value": None,
        "dosage_instruction_max_dose_per_administration_unit": None,
        "dosage_instruction_max_dose_per_administration_system": None,
        "dosage_instruction_max_dose_per_administration_code": None,
        "dosage_instruction_max_dose_per_lifetime_value": None,
        "dosage_instruction_max_dose_per_lifetime_unit": None,
        "dosage_instruction_max_dose_per_lifetime_system": None,
        "dosage_instruction_max_dose_per_lifetime_code": None,
    }
]


class MedicationDispenseDosageInstructionTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'MedicationDispense' resource.

       This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationDispense' resource.
    It predefines the resource type as 'MedicationDispense'
    and initializes the resource with the specific 'MedicationDispense' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationDispense'.

        resource (dict): The raw FHIR 'MedicationDispense' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationDispense' resource payload.
    """

    resource_type = "MedicationDispense"
    resource_subtype = "dosage_instruction"
    transformer = MedicationDispenseDosageInstructionTransformer
    expected_table_name = "medication_dispense_dosage_instruction"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
