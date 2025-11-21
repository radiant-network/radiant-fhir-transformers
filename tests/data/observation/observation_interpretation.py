"""
Test helper class for FHIR resource type Observation subtype Interpretation
"""

from radiant_fhir_transform_cli.transform.classes import (
    ObservationInterpretationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "interpretation_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
        "interpretation_coding_code": "NEG",
        "interpretation_coding_display": "Negative",
        "interpretation_text": None,
        "id": "d567996a-7fe2-4ad1-ba7f-fdcd7eb14e4b",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
]


class ObservationInterpretationTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "interpretation"
    transformer = ObservationInterpretationTransformer
    expected_table_name = "observation_interpretation"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
