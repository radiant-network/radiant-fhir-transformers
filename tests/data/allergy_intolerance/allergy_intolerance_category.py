"""
Test helper class for FHIR resource type AllergyIntolerance subtype category
"""

from radiant_fhir_transform_cli.transform.classes.allergy_intolerance import (
    AllergyIntoleranceCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "category": "food",
        "id": "edbc7300-fe00-4900-b96b-17ea12e78b95",
        "allergy_intolerance_id": "example_ai",
    },
]


class AllergyIntoleranceCategoryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category"
    transformer = AllergyIntoleranceCategoryTransformer
    expected_table_name = "allergy_intolerance_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
