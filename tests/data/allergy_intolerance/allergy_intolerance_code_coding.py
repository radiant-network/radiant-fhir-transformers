"""
Test helper class for FHIR resource type AllergyIntolerance subtype Verification Status Coding
"""

from radiant_fhir_transform_cli.transform.classes.allergy_intolerance.allergy_intolerance_code_coding import (
    AllergyIntoleranceCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://snomed.info/sct",
        "code_coding_code": "227493005",
        "code_coding_display": "Cashew nuts",
        "id": "04eb3a47-73eb-4eb7-9a1c-a4473fa4f5e6",
        "allergy_intolerance_id": "example_ai",
    },
]


class AllergyIntoleranceCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = AllergyIntoleranceCodeCodingTransformer
    expected_table_name = "allergy_intolerance_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
