"""
Test helper class for FHIR resource type Observation subtype Component
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationComponentTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "component_code_coding": [
            {
                "system": "http://loinc.org",
                "code": "8480-6",
                "display": "Systolic blood pressure",
            }
        ],
        "component_code_text": "Systolic blood pressure",
        "component_value_quantity_value": None,
        "component_value_quantity_comparator": None,
        "component_value_quantity_unit": None,
        "component_value_quantity_system": None,
        "component_value_quantity_code": None,
        "component_value_codeable_concept_coding": None,
        "component_value_codeable_concept_text": None,
        "component_value_string": None,
        "component_value_boolean": None,
        "component_value_integer": None,
        "component_value_range_low_value": 2,
        "component_value_range_low_unit": "test",
        "component_value_range_low_system": None,
        "component_value_range_low_code": None,
        "component_value_range_high_value": 6,
        "component_value_range_high_unit": "test",
        "component_value_range_high_system": None,
        "component_value_range_high_code": None,
        "component_value_ratio_numerator_value": None,
        "component_value_ratio_numerator_comparator": None,
        "component_value_ratio_numerator_unit": None,
        "component_value_ratio_numerator_system": None,
        "component_value_ratio_numerator_code": None,
        "component_value_ratio_denominator_value": None,
        "component_value_ratio_denominator_comparator": None,
        "component_value_ratio_denominator_unit": None,
        "component_value_ratio_denominator_system": None,
        "component_value_ratio_denominator_code": None,
        "component_value_sampled_data_origin_value": None,
        "component_value_sampled_data_origin_unit": None,
        "component_value_sampled_data_origin_system": None,
        "component_value_sampled_data_origin_code": None,
        "component_value_sampled_data_period": None,
        "component_value_sampled_data_factor": None,
        "component_value_sampled_data_lower_limit": None,
        "component_value_sampled_data_upper_limit": None,
        "component_value_sampled_data_dimensions": None,
        "component_value_sampled_data_data": None,
        "component_value_time": None,
        "component_value_date_time": None,
        "component_value_period_start": None,
        "component_value_period_end": None,
        "component_data_absent_reason_coding": None,
        "component_data_absent_reason_text": None,
        "component_interpretation": None,
        "component_reference_range": None,
    },
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "component_code_coding": [
            {
                "system": "http://loinc.org",
                "code": "8462-4",
                "display": "Diastolic blood pressure",
            }
        ],
        "component_code_text": "Diastolic blood pressure",
        "component_value_quantity_value": None,
        "component_value_quantity_comparator": None,
        "component_value_quantity_unit": None,
        "component_value_quantity_system": None,
        "component_value_quantity_code": None,
        "component_value_codeable_concept_coding": None,
        "component_value_codeable_concept_text": None,
        "component_value_string": None,
        "component_value_boolean": None,
        "component_value_integer": None,
        "component_value_range_low_value": 1,
        "component_value_range_low_unit": "test1",
        "component_value_range_low_system": None,
        "component_value_range_low_code": None,
        "component_value_range_high_value": 3,
        "component_value_range_high_unit": "test1",
        "component_value_range_high_system": None,
        "component_value_range_high_code": None,
        "component_value_ratio_numerator_value": None,
        "component_value_ratio_numerator_comparator": None,
        "component_value_ratio_numerator_unit": None,
        "component_value_ratio_numerator_system": None,
        "component_value_ratio_numerator_code": None,
        "component_value_ratio_denominator_value": None,
        "component_value_ratio_denominator_comparator": None,
        "component_value_ratio_denominator_unit": None,
        "component_value_ratio_denominator_system": None,
        "component_value_ratio_denominator_code": None,
        "component_value_sampled_data_origin_value": None,
        "component_value_sampled_data_origin_unit": None,
        "component_value_sampled_data_origin_system": None,
        "component_value_sampled_data_origin_code": None,
        "component_value_sampled_data_period": None,
        "component_value_sampled_data_factor": None,
        "component_value_sampled_data_lower_limit": None,
        "component_value_sampled_data_upper_limit": None,
        "component_value_sampled_data_dimensions": None,
        "component_value_sampled_data_data": None,
        "component_value_time": None,
        "component_value_date_time": None,
        "component_value_period_start": None,
        "component_value_period_end": None,
        "component_data_absent_reason_coding": None,
        "component_data_absent_reason_text": None,
        "component_interpretation": None,
        "component_reference_range": None,
    },
]


class ObservationComponentTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "component"
    transformer = ObservationComponentTransformer
    expected_table_name = "observation_component"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
