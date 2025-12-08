"""
Test helper class for FHIR resource type Observation subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://loinc.org",
        "code_coding_code": "94500-6",
        "code_coding_display": "SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory system specimen by NAA with probe detection",
        "id": "bf6c4e70-7585-4cb6-8149-6d4231a44374",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
    {
        "code_coding_system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.600012",
        "code_coding_code": "RCOVID",
        "code_coding_display": None,
        "id": "5c3daa27-bf57-4f3b-bcc7-e49288527802",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
    {
        "code_coding_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.768282",
        "code_coding_code": "123090220",
        "code_coding_display": "Rapid Sars-CoV-2",
        "id": "9fb2fb6c-c275-4aa9-9917-5ba95b0d1c9c",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
]


class ObservationCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = ObservationCodeCodingTransformer
    expected_table_name = "observation_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
