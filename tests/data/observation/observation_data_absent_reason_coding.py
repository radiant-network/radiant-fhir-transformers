"""
Test helper class for FHIR resource type Observation subtype DataAbsentReason Coding
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationDataAbsentReasonCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "data_absent_reason_coding_system": "http://terminology.hl7.org/CodeSystem/data-absent-reason",
        "data_absent_reason_coding_code": "unknown",
        "data_absent_reason_coding_display": "Unknown",
        "id": "7800f5e1-1255-42fe-92dc-18ce0b286c79",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
]


class ObservationDataAbsentReasonCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "data_absent_reason_coding"
    transformer = ObservationDataAbsentReasonCodingTransformer
    expected_table_name = "observation_data_absent_reason_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
