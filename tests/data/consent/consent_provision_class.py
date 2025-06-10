"""
Test helper class for FHIR resource type Consent subtype Provision Class
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentProvisionClassTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "consent_id": "consent-example-basic",
        "provision_class_system": "http://hl7.org/fhir/ValueSet/consent-content-class",
        "provision_class_code": "urn:ihe:pcc:xphr:2007",
        "provision_class_display": "Personal Health Records. Also known as HL7 CCD and HITSP C32",
    },
]


class ConsentProvisionClassTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "provision_class"
    transformer = ConsentProvisionClassTransformer
    expected_table_name = "consent_provision_class"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
