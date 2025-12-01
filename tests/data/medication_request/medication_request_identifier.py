"""
Test helper class for FHIR resource type MedicationRequest subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": "official",
        "identifier_system": "http://www.bmc.nl/portal/prescriptions",
        "identifier_value": "12345689",
        "id": "e5028d39-e91d-414d-91e5-5cadc965065c",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = MedicationRequestIdentifierTransformer
    expected_table_name = "medication_request_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
