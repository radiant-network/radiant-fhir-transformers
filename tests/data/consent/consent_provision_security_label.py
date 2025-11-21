"""
Test helper class for FHIR resource type Consent subtype Provision SecurityLabel
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentProvisionSecurityLabelTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provision_security_label_system": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality",
        "provision_security_label_code": "N",
        "provision_security_label_display": None,
        "id": "8675fc37-1674-4bf2-b79b-3d0ff5bc5f4b",
        "consent_id": "consent-example-basic",
    },
]


class ConsentProvisionSecurityLabelTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "provision_security_label"
    transformer = ConsentProvisionSecurityLabelTransformer
    expected_table_name = "consent_provision_security_label"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
