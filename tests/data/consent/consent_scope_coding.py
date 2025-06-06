"""
Test helper class for FHIR resource type Consent subtype Scope Coding
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentScopeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "consent_id": "consent-example-basic",
        "scope_coding_system": "http://terminology.hl7.org/CodeSystem/consentscope",
        "scope_coding_code": "patient-privacy",
        "scope_coding_display": None,
    },
]


class ConsentScopeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "scope_coding"
    transformer = ConsentScopeCodingTransformer
    expected_table_name = "consent_scope_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
