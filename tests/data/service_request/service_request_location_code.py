"""
Test helper class for FHIR resource type ServiceRequest subtype LocationCode
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestLocationCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "service_request_id": "di_abcd_efg",
        "location_code_coding": None,
        "location_code_text": "Pediatrics",
        "location_code_type": None,
    },
]


class ServiceRequestLocationCodeTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'ServiceRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'ServiceRequest' resource.

    It predefines the resource type as 'ServiceRequest'
    and initializes the resource with the specific 'ServiceRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'ServiceRequest'.

        resource (dict): The raw FHIR 'ServiceRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'ServiceRequest' resource payload.
    """

    resource_type = "ServiceRequest"
    resource_subtype = "location_code"
    transformer = ServiceRequestLocationCodeTransformer
    expected_table_name = "service_request_location_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
