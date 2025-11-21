"""
Test helper class for FHIR resource type Consent subtype Provision Actor
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentProvisionActorTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provision_actor_role_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
        "provision_actor_role_coding_code": "PRCP",
        "provision_actor_role_text": None,
        "provision_actor_reference_reference": "Practitioner/13",
        "provision_actor_reference_type": None,
        "provision_actor_reference_display": None,
        "id": "3dd5e243-cef5-40ce-b410-0039a1f1632b",
        "consent_id": "consent-example-basic",
    },
]


class ConsentProvisionActorTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "provision_actor"
    transformer = ConsentProvisionActorTransformer
    expected_table_name = "consent_provision_actor"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
