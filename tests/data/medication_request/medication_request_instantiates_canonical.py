"""
Test helper class for FHIR resource type MedicationRequest subtype InstantiatesCanonical
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestInstantiatesCanonicalTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "instantiates_canonical": "canonical",
        "id": "b4bfffe8-405a-40d3-b6fb-f10559f3b81b",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestInstantiatesCanonicalTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'MedicationRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationRequest' resource.

    It predefines the resource type as 'MedicationRequest'
    and initializes the resource with the specific 'MedicationRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationRequest'.

        resource (dict): The raw FHIR 'MedicationRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationRequest' resource payload.
    """

    resource_type = "MedicationRequest"
    resource_subtype = "instantiates_canonical"
    transformer = MedicationRequestInstantiatesCanonicalTransformer
    expected_table_name = "medication_request_instantiates_canonical"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
