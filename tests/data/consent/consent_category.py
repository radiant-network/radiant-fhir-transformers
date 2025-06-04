"""
Test helper class for FHIR resource type Consent subtype Category
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "consent_id": "consent-example-basic",
        "category_coding": [{"system": "http://loinc.org", "code": "59284-0"}],
        "category_text": None,
    },
]


class ConsentCategoryTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Consent' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Consent' resource.

    It predefines the resource type as 'Consent'
    and initializes the resource with the specific 'Consent' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Consent'.

        resource (dict): The raw FHIR 'Consent' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Consent' resource payload.
    """

    resource_type = "Consent"
    resource_subtype = "category"
    transformer = ConsentCategoryTransformer
    expected_table_name = "consent_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
