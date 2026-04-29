"""
Test helper class for FHIR resource type ServiceRequest subtype asNeededCodeableConceptCoding
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestAsNeededCodeableConceptCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "as_needed_codeable_concept_coding_system": "http://mysystem.org",
        "as_needed_codeable_concept_coding_code": "123-yes",
        "as_needed_codeable_concept_coding_display": None,
        "id": "a36cb934-243e-4931-b2d7-e6f26e1e72e0",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestAsNeededCodeableConceptCodingTestHelper(FhirResourceTestHelper):
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
    resource_component = "as_needed_codeable_concept_coding"
    transformer = ServiceRequestAsNeededCodeableConceptCodingTransformer
    expected_table_name = "service_request_as_needed_codeable_concept_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
