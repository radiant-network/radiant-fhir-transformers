"""
Test helper class for FHIR resource type Observation subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "identifier_use": "official",
        "identifier_type_text": None,
        "identifier_system": "http://www.bmc.nl/zorgportal/identifiers/observations",
        "identifier_value": "6326",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class ObservationIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = ObservationIdentifierTransformer
    expected_table_name = "observation_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
