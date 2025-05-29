"""
Test helper class for FHIR resource type AllergyIntolerance subtype Verification Status Coding
"""

from radiant_fhir_transform_cli.transform.classes.allergy_intolerance.allergy_intolerance_verification_status_coding import (
    AllergyIntoleranceVerificationStatusCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "allergy_intolerance_id": "example_ai",
        "verification_status_coding_system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-verification",
        "verification_status_coding_code": "confirmed",
        "verification_status_coding_display": "Confirmed",
    },
]


class AllergyIntoleranceVerificationStatusCodingTestHelper(
    FhirResourceTestHelper
):
    """
    A helper class for testing transformations of the FHIR 'AllergyIntolerance' resource.
    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'AllergyIntolerance' resource.
    It predefines the resource type as 'AllergyIntolerance'
    and initializes the resource with the specific 'AllergyIntolerance' resource payload
    and its expected transformation output.
    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'AllergyIntolerance'.
        resource (dict): The raw FHIR 'AllergyIntolerance' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'AllergyIntolerance' resource payload.
    """

    resource_type = "AllergyIntolerance"
    resource_subtype = "verification_status_coding"
    transformer = AllergyIntoleranceVerificationStatusCodingTransformer
    expected_table_name = "allergy_intolerance_verification_status_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
