"""
Test helper class for FHIR resource type ServiceRequest subtype category
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "category_coding": {
            "system": "http://snomed.info/sct",
            "code": "103696004",
            "display": "Patient referral to specialist",
        },
        "category_text": None,
        "id": "d728baee-b087-4ee6-9de3-77f82b355c97",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestCategoryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category"
    transformer = ServiceRequestCategoryTransformer
    expected_table_name = "service_request_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
