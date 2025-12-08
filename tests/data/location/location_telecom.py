"""
Test helper class for FHIR resource type Location subtype Telecom
"""

from radiant_fhir_transform_cli.transform.classes.location import (
    LocationTelecomTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .location_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "telecom_system": "phone",
        "telecom_value": "215-590-5223",
        "telecom_use": None,
        "telecom_rank": 1,
        "telecom_period_start": None,
        "telecom_period_end": None,
        "id": "667f332a-934b-43ba-92b8-81f79fe8913c",
        "location_id": "3ad0687e-f477-468c-afd5-fcc2bf897819",
    },
    {
        "telecom_system": "fax",
        "telecom_value": "215-590-4460",
        "telecom_use": None,
        "telecom_rank": None,
        "telecom_period_start": None,
        "telecom_period_end": None,
        "id": "b52ef605-d11e-4679-9a08-32defc0a3a97",
        "location_id": "3ad0687e-f477-468c-afd5-fcc2bf897819",
    },
]


class LocationTelecomTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Location' resource.
    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Location' resource.
    It predefines the resource type as 'Location'
    and initializes the resource with the specific 'Location' resource payload
    and its expected transformation output.
    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Location'.
        resource (dict): The raw FHIR 'Location' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Location' resource payload.
    """

    resource_type = "Location"
    resource_subtype = "telecom"
    transformer = LocationTelecomTransformer
    expected_table_name = "location_telecom"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
