"""
Test helper class for FHIR resource type MedicationRequest subtype Substitution Reason Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestSubstitutionReasonCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_request_id": "medrx0301",
        "substitution_reason_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
        "substitution_reason_coding_code": "FP",
        "substitution_reason_coding_display": "formulary policy",
    }
]


class MedicationRequestSubstitutionReasonCodingTestHelper(
    FhirResourceTestHelper
):
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
    resource_subtype = "substitution_reason_coding"
    transformer = MedicationRequestSubstitutionReasonCodingTransformer
    expected_table_name = "medication_request_substitution_reason_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
