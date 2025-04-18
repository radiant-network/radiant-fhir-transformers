"""
Test helper class for FHIR resource type Observation subtype extension
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationExtensionTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "extension_value_identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.77777",
        "extension_value_identifier_value": "887",
        "extension_url": "http://open.epic.com/FHIR/StructureDefinition/extension/template-id",
    },
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "extension_value_identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.707684",
        "extension_value_identifier_value": "555",
        "extension_url": "http://open.epic.com/FHIR/StructureDefinition/extension/template-id",
    },
]


class ObservationExtensionTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "extension"
    transformer = ObservationExtensionTransformer

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
