"""
Test helper class for FHIR resource type Organization subtype Contact
"""

from radiant_fhir_transform_cli.transform.classes.organization import (
    OrganizationContactTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .organization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "contact_purpose_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
                "code": "PRESS",
            }
        ],
        "contact_purpose_text": None,
        "contact_name_use": None,
        "contact_name_text": None,
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_telecom": [{"system": "phone", "value": "022-655 2334"}],
        "contact_address_use": None,
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_line": None,
        "contact_address_city": None,
        "contact_address_district": None,
        "contact_address_state": None,
        "contact_address_postal_code": None,
        "contact_address_country": None,
        "contact_address_period_start": None,
        "contact_address_period_end": None,
    },
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "contact_purpose_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
                "code": "PATINF",
            }
        ],
        "contact_purpose_text": None,
        "contact_name_use": None,
        "contact_name_text": None,
        "contact_name_family": None,
        "contact_name_given": None,
        "contact_name_prefix": None,
        "contact_name_suffix": None,
        "contact_name_period_start": None,
        "contact_name_period_end": None,
        "contact_telecom": [{"system": "phone", "value": "022-655 2335"}],
        "contact_address_use": None,
        "contact_address_type": None,
        "contact_address_text": None,
        "contact_address_line": None,
        "contact_address_city": None,
        "contact_address_district": None,
        "contact_address_state": None,
        "contact_address_postal_code": None,
        "contact_address_country": None,
        "contact_address_period_start": None,
        "contact_address_period_end": None,
    },
]


class OrganizationContactTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Organization' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Organization' resource.

    It predefines the resource type as 'Organization'
    and initializes the resource with the specific 'Organization' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Organization'.

        resource (dict): The raw FHIR 'Organization' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Organization' resource payload.
    """

    resource_type = "Organization"
    resource_subtype = "contact"
    transformer = OrganizationContactTransformer
    expected_table_name = "organization_contact"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
