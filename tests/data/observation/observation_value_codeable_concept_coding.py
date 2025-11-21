"""
Test helper class for FHIR resource type Observation subtype ValueCodeableConcept Coding
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationValueCodeableConceptCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "value_codeable_concept_coding_system": "http://snomed.info/sct_1",
        "value_codeable_concept_coding_code": "260415000",
        "value_codeable_concept_coding_display": None,
        "id": "6267e691-3b38-4506-b9b5-ad473ca7a212",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
    {
        "value_codeable_concept_coding_system": "http://snomed.info/sct_2",
        "value_codeable_concept_coding_code": "9999999",
        "value_codeable_concept_coding_display": None,
        "id": "d9511f97-173d-411e-8f80-2cff7ed4bece",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
    {
        "value_codeable_concept_coding_system": "http://snomed.info/sct_3",
        "value_codeable_concept_coding_code": "8888888",
        "value_codeable_concept_coding_display": None,
        "id": "64462a08-2853-48e3-9c83-f67d7c703564",
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    },
]


class ObservationValueCodeableConceptCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "value_codeable_concept_coding"
    transformer = ObservationValueCodeableConceptCodingTransformer
    expected_table_name = "observation_value_codeable_concept_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
