"""
Test helper class for FHIR resource type Organization subtype Telecom
"""

from radiant_fhir_transform_cli.transform.classes.organization import (
    OrganizationTelecomTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .organization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "telecom_system": "phone",
        "telecom_value": "215-590-3326",
        "telecom_use": "work",
        "telecom_rank": None,
        "telecom_period_start": None,
        "telecom_period_end": None,
    },
    {
        "organization_id": "2.16.840.1.113883.19.5",
        "telecom_system": "fax",
        "telecom_value": "215-590-3606",
        "telecom_use": "work",
        "telecom_rank": None,
        "telecom_period_start": None,
        "telecom_period_end": None,
    },
]


class OrganizationTelecomTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "telecom"
    transformer = OrganizationTelecomTransformer
    expected_table_name = "organization_telecom"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
