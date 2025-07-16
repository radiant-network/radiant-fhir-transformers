"""
Test helper class for FHIR resource type Observation subtype performer
"""

from radiant_fhir_transform_cli.transform.classes import (
    ObservationBasedOnTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "based_on_reference": "eKSdPx93PPg7jLqFtgAKjJbL1RWvYEkyba5u.yiQaXZE3",
        "based_on_reference_type": "ServiceRequest",
        "based_on_display": "Rapid SARS-CoV-2 PCR",
    },
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "based_on_reference": "elkj;lskdjf;ljl;ghghhhddddddjj.yiQaXZE3",
        "based_on_reference_type": "ServiceRequest",
        "based_on_display": "Rapid TESTER",
    },
]


class ObservationBasedOnTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "based_on"
    transformer = ObservationBasedOnTransformer
    expected_table_name = "observation_based_on"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
