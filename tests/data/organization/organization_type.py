"""
Test helper class for FHIR resource type Organization subtype Type
"""

from radiant_fhir_transform_cli.transform.classes.organization import (
    OrganizationTypeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .organization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "type_coding": [
            {
                "system": "urn:oid:2.16.840.1.113883.2.4.15.1060",
                "code": "V6",
                "display": "University Medical Hospital",
            },
            {
                "system": "http://terminology.hl7.org/CodeSystem/organization-type",
                "code": "prov",
                "display": "Healthcare Provider",
            },
        ],
        "type_text": None,
    },
]


class OrganizationTypeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "type"
    transformer = OrganizationTypeTransformer
    expected_table_name = "organization_type"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
