"""
Test helper class for FHIR resource type MedicationRequest subtype ReasonCode
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_code_text": "Cytopenia",
        "id": "1c62f09f-69ce-4008-954b-03db4da721e1",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Immunocompromised state",
        "id": "7d8faa5b-6257-4031-8586-96423af2e21f",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Need for pneumocystis prophylaxis",
        "id": "b694953e-de96-4948-8564-611b666dcc3e",
        "medication_request_id": "medrx0301",
    },
    {
        "reason_code_text": "Medulloblastoma",
        "id": "7b901194-ecc8-4e38-9cea-570e464b8e46",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestReasonCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_code"
    transformer = MedicationRequestReasonCodeTransformer
    expected_table_name = "medication_request_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
