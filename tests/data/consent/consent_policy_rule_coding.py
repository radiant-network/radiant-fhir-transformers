"""
Test helper class for FHIR resource type Consent subtype PolicyRule Coding
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentPolicyRuleCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "policy_rule_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "policy_rule_coding_code": "OPTIN",
        "policy_rule_coding_display": None,
        "id": "cc295ba7-4405-42d7-8dc3-e17033bf5cf0",
        "consent_id": "consent-example-basic",
    },
]


class ConsentPolicyRuleCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "policy_rule_coding"
    transformer = ConsentPolicyRuleCodingTransformer
    expected_table_name = "consent_policy_rule_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
