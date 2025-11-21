"""
Test helper class for FHIR resource type ServiceRequest subtype reasonCode
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "service_request_id": "di_abcd_efg",
        "reason_code_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "90831000119105",
                "display": "Check for metastatic disease",
            }
        ],
        "reason_code_text": "Check for metastatic disease",
        "id": "0bec9d4e-a32b-4289-b016-349209e261ba",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestReasonCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_codee"
    transformer = ServiceRequestReasonCodeTransformer
    expected_table_name = "service_request_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
