"""
Test helper class for FHIR resource type ServiceRequest subtype orderDetail
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestOrderDetailTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "order_detail_coding": {
            "system": "http://snomed.info/sct",
            "code": "243144002",
            "display": "Patient triggered inspiratory assistance (procedure)",
        },
        "order_detail_text": "IPPB",
        "id": "3cbc1d6e-e409-4359-8c4f-4b7464c6b7b7",
        "service_request_id": "di_abcd_efg",
    },
    {
        "order_detail_coding": None,
        "order_detail_text": " Initial Settings : Sens: -1 cm H20 Pressure 15 cm H2O moderate flow:  Monitor VS every 15 minutes x 4 at the start of mechanical ventilation, then routine for unit OR every 5 hr",
        "id": "6fcb6e6d-1f90-45c1-9797-b7e239472f8f",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestOrderDetailTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "order_detail"
    transformer = ServiceRequestOrderDetailTransformer
    expected_table_name = "service_request_order_detail"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
