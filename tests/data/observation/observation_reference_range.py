"""
Test helper class for FHIR resource type Observation subtype ReferenceRange
"""

from radiant_fhir_transform_cli.transform.classes import (
    ObservationReferenceRangeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reference_range_low_value": None,
        "reference_range_low_unit": None,
        "reference_range_low_system": None,
        "reference_range_low_code": None,
        "reference_range_high_value": None,
        "reference_range_high_unit": None,
        "reference_range_high_system": None,
        "reference_range_high_code": None,
        "reference_range_type_coding": None,
        "reference_range_type_text": None,
        "reference_range_applies_to": None,
        "reference_range_age_low_value": None,
        "reference_range_age_low_unit": None,
        "reference_range_age_low_system": None,
        "reference_range_age_low_code": None,
        "reference_range_age_high_value": None,
        "reference_range_age_high_unit": None,
        "reference_range_age_high_system": None,
        "reference_range_age_high_code": None,
        "reference_range_text": "Negative",
        "id": "6769ff2b-30a4-4c83-b7ca-c950a6733d1c",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
]


class ObservationReferenceRangeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reference_range"
    transformer = ObservationReferenceRangeTransformer
    expected_table_name = "observation_reference_range"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
