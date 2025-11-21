"""
Test helper class for FHIR resource type ServiceRequest subtype codeCoding
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://loinc.org",
        "code_coding_code": "24627-2",
        "code_coding_display": None,
        "id": "a36cb934-243e-4931-b2d7-e6f26e1e72e0",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = ServiceRequestCodeCodingTransformer
    expected_table_name = "service_request_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
