"""
Test helper class for FHIR resource type Observation
"""

from radiant_fhir_transform_cli.transform.classes.observation.observation import (
    ObservationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "resource_type": "Observation",
        "status": "final",
        "code_text": "Rapid Sars-CoV-2",
        "subject_reference": "evrlLhFNe5BfHZQD39Kr9nfIA0e.TcZOdE0gOPoRXlGs3",
        "subject_reference_type": "Patient",
        "subject_display": "CareEverywhere,Sammy",
        "encounter_reference": "e.mnIF2M9LQgwkDzhr2PCKA3",
        "encounter_reference_type": "Encounter",
        "encounter_identifier_use": "usual",
        "encounter_identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.698084.8",
        "encounter_identifier_value": "8200106334",
        "encounter_display": "Hospital Encounter",
        "effective_date_time": "2024-01-29T16:46:00Z",
        "effective_period_start": None,
        "effective_period_end": None,
        "effective_timing_repeat_bounds_duration_value": None,
        "effective_timing_repeat_bounds_duration_comparator": None,
        "effective_timing_repeat_bounds_duration_unit": None,
        "effective_timing_repeat_bounds_duration_system": None,
        "effective_timing_repeat_bounds_duration_code": None,
        "effective_timing_repeat_bounds_range_low_value": None,
        "effective_timing_repeat_bounds_range_low_unit": None,
        "effective_timing_repeat_bounds_range_low_system": None,
        "effective_timing_repeat_bounds_range_low_code": None,
        "effective_timing_repeat_bounds_range_high_value": None,
        "effective_timing_repeat_bounds_range_high_unit": None,
        "effective_timing_repeat_bounds_range_high_system": None,
        "effective_timing_repeat_bounds_range_high_code": None,
        "effective_timing_repeat_bounds_period_start": None,
        "effective_timing_repeat_bounds_period_end": None,
        "effective_timing_repeat_count": None,
        "effective_timing_repeat_count_max": None,
        "effective_timing_repeat_duration": None,
        "effective_timing_repeat_duration_max": None,
        "effective_timing_repeat_duration_unit": None,
        "effective_timing_repeat_frequency": None,
        "effective_timing_repeat_frequency_max": None,
        "effective_timing_repeat_period": None,
        "effective_timing_repeat_period_max": None,
        "effective_timing_repeat_period_unit": None,
        "effective_timing_repeat_offset": None,
        "effective_timing_code_text": None,
        "effective_instant": None,
        "issued": "2024-01-29T16:46:57Z",
        "value_quantity_value": None,
        "value_quantity_comparator": None,
        "value_quantity_unit": None,
        "value_quantity_system": None,
        "value_quantity_code": None,
        "value_codeable_concept_text": "Negative",
        "value_string": None,
        "value_boolean": None,
        "value_integer": None,
        "value_range_low_value": None,
        "value_range_low_unit": None,
        "value_range_low_system": None,
        "value_range_low_code": None,
        "value_range_high_value": None,
        "value_range_high_unit": None,
        "value_range_high_system": None,
        "value_range_high_code": None,
        "value_ratio_numerator_value": None,
        "value_ratio_numerator_comparator": None,
        "value_ratio_numerator_unit": None,
        "value_ratio_numerator_system": None,
        "value_ratio_numerator_code": None,
        "value_ratio_denominator_value": None,
        "value_ratio_denominator_comparator": None,
        "value_ratio_denominator_unit": None,
        "value_ratio_denominator_system": None,
        "value_ratio_denominator_code": None,
        "value_sampled_data_origin_value": None,
        "value_sampled_data_origin_unit": None,
        "value_sampled_data_origin_system": None,
        "value_sampled_data_origin_code": None,
        "value_sampled_data_period": None,
        "value_sampled_data_factor": None,
        "value_sampled_data_lower_limit": None,
        "value_sampled_data_upper_limit": None,
        "value_sampled_data_dimensions": None,
        "value_sampled_data_data": None,
        "value_time": None,
        "value_date_time": None,
        "value_period_start": None,
        "value_period_end": None,
        "data_absent_reason_text": None,
        "body_site_text": None,
        "method_text": None,
        "specimen_reference": "eofvi8EpxgTC9958OEt3Xuw3",
        "specimen_reference_type": "Specimen",
        "specimen_display": "Specimen 24U-ID-0290004",
        "device_reference": "device",
        "device_type": None,
        "device_display": None,
    }
]


class ObservationTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Observation' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Observation' resource.

    It predefines the resource type as 'Observation'
    and initializes the resource with the specific 'Observation' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Observation'.

        resource (dict): The raw FHIR 'Observation' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Observation' resource payload.
    """

    resource_type = "Observation"
    resource_subtype = None
    transformer = ObservationTransformer
    expected_table_name = "observation"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
