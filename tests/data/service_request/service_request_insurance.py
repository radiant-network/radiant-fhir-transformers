"""
Test helper class for FHIR resource type ServiceRequest subtype insurance
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestInsuranceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "service_request_id": "di_abcd_efg",
        "insurance_reference": "Coverage/abc-123",
        "insurance_display": "BCBS of Atlantis",
        "insurance_type": None,
    },
]


class ServiceRequestInsuranceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "insurance"
    transformer = ServiceRequestInsuranceTransformer
    expected_table_name = "service_request_insurance"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
