"""
Test helper class for FHIR resource type Observation subtype EffectiveTiming Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationEffectiveTimingCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "effective_timing_code_coding_system": "http://terminology.hl7.org/CodeSystem/v3-GTSAbbreviation",
        "effective_timing_code_coding_code": "PM",
        "effective_timing_code_coding_display": "PM",
        "id": "19e42f19-6855-44a0-8a90-f8f7b3cb55ce",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
]


class ObservationEffectiveTimingCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "effective_timing_code_coding"
    transformer = ObservationEffectiveTimingCodeCodingTransformer
    expected_table_name = "observation_effective_timing_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
