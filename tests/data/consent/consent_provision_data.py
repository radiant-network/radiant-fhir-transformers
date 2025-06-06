"""
Test helper class for FHIR resource type Consent subtype Provision Data
"""

from radiant_fhir_transform_cli.transform.classes.consent import (
    ConsentProvisionDataTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .consent_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "consent_id": "consent-example-basic",
        "provision_data_meaning": "authoredby",
        "provision_data_reference_reference": "DocumentReference/documentreference",
        "provision_data_reference_type": None,
        "provision_data_reference_display": None,
    },
]


class ConsentProvisionDataTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "provision_data"
    transformer = ConsentProvisionDataTransformer
    expected_table_name = "consent_provision_data"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
