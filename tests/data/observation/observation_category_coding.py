"""
Test helper class for FHIR resource type Observation subtype Category Coding
"""

from radiant_fhir_transform_cli.transform.classes.observation.observation_category_coding import (
    ObservationCategoryCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "category_coding_system": "http://terminology.hl7.org/CodeSystem/observation-category",
        "category_coding_code": "laboratory",
        "category_coding_display": "Laboratory",
    },
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "category_coding_system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.798268.30",
        "category_coding_code": "lab",
        "category_coding_display": None,
    },
]


class ObservationCategoryCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category_coding"
    transformer = ObservationCategoryCodingTransformer
    expected_table_name = "observation_category_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
