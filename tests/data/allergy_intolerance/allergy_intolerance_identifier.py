"""
Test helper class for FHIR resource type AllergyIntolerance subtype identifier
"""

from radiant_fhir_transform_cli.transform.classes import (
    AllergyIntoleranceIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance import RESOURCE

EXPECTED_OUTPUT = [
    {
        "allergy_intolerance_id": "example_ai",
        "identifier_type_text": None,
        "identifier_system": "http://acme.com/ids/patients/risks",
        "identifier_value": "49476534",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "identifier_use": None,
    },
]


class AllergyIntoleranceIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = AllergyIntoleranceIdentifierTransformer
    expected_table_name = "allergy_intolerance_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
