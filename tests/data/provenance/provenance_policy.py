"""
Test helper class for FHIR resource type Provenance subtype Policy
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenancePolicyTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "policy": "http://acme.com/fhir/Consent/25",
        "id": "3814272c-3305-46f3-9b74-b24ba2643fc4",
        "provenance_id": "provenance",
    },
]


class ProvenancePolicyTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Provenance' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Provenance' resource.

    It predefines the resource type as 'Provenance'
    and initializes the resource with the specific 'Provenance' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Provenance'.

        resource (dict): The raw FHIR 'Provenance' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Provenance' resource payload.
    """

    resource_type = "Provenance"
    resource_subtype = "policy"
    transformer = ProvenancePolicyTransformer
    expected_table_name = "provenance_policy"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
