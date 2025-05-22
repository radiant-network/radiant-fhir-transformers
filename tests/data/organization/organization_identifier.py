"""
Test helper class for FHIR resource type Organization subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.organization import (
    OrganizationIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .organization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "identifier_use": "usual",
        "identifier_type_text": None,
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.8553241",
        "identifier_value": "7968",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "identifier_use": "usual",
        "identifier_type_text": None,
        "identifier_system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.8553242",
        "identifier_value": "PH0453",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "identifier_use": "usual",
        "identifier_type_text": "NPI",
        "identifier_system": "http://hl7.org/fhir/sid/us-npi",
        "identifier_value": "1215921457",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class OrganizationIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = OrganizationIdentifierTransformer
    expected_table_name = "organization_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
