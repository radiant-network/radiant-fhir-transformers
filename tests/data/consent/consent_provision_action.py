"""
Test helper class for FHIR resource type Consent subtype Provision Action
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentProvisionActionTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provision_action_coding_system": "http://terminology.hl7.org/CodeSystem/consentaction",
        "provision_action_coding_code": "access",
        "provision_action_text": None,
        "id": "4396313e-51ed-43b1-8f01-71cd816a4b07",
        "consent_id": "consent-example-basic",
    },
]


class ConsentProvisionActionTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "provision_action"
    transformer = ConsentProvisionActionTransformer
    expected_table_name = "consent_provision_action"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
