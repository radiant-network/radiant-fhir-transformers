"""
Test helper class for FHIR resource type Location
"""

from radiant_fhir_transform_cli.transform.classes.location import (
    LocationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .location_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "address_line": "550 South Goddard Blvd",
        "id": "3ad0687e-f477-468c-afd5-fcc2bf897819",
        "resource_type": "Location",
        "status": "active",
        "operational_status_system": "http://terminology.hl7.org/CodeSystem/v2-0116",
        "operational_status_code": "H",
        "operational_status_display": "Housekeeping",
        "name": "KOP Nutrition",
        "description": "Second floor of the Old South Wing, formerly in use by Psychiatry",
        "mode": "instance",
        "address_use": None,
        "address_type": None,
        "address_text": None,
        "address_city": "King of Prussia",
        "address_district": None,
        "address_state": "Pennsylvania",
        "address_postal_code": "19406",
        "address_country": "United States",
        "address_period_start": None,
        "address_period_end": None,
        "physical_type_text": None,
        "position_longitude": None,
        "position_latitude": None,
        "position_altitude": None,
        "managing_organization_reference": "Organization/organization",
        "managing_organization_type": None,
        "managing_organization_display": "Organization",
        "part_of_reference": "Location/location",
        "part_of_type": None,
        "part_of_display": "Location",
        "availability_exceptions": None,
    },
]


class LocationTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = LocationTransformer
    expected_table_name = "location"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
