"""
Test helper class for FHIR resource type Consent subtype Verification
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentVerificationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "verification_verified": True,
        "verification_verified_with_reference": None,
        "verification_verified_with_type": None,
        "verification_verified_with_display": None,
        "verification_verification_date": "2015-10-10",
        "id": "212fd254-9b24-4b45-87e7-7be734d41dc0",
        "consent_id": "consent-example-basic",
    },
]


class ConsentVerificationTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "verification"
    transformer = ConsentVerificationTransformer
    expected_table_name = "consent_verification"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
