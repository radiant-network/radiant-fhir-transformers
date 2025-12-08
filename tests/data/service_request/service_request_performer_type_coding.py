"""
Test helper class for FHIR resource type ServiceRequest subtype performerTypeCoding
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestPerformerTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "performer_type_coding_system": "http://orionhealth.com/fhir/apps/specialties",
        "performer_type_coding_version": None,
        "performer_type_coding_code": "ent",
        "performer_type_coding_display": "ENT",
        "performer_type_coding_user_selected": None,
        "id": "cfa07124-1a64-46dc-ac56-ec4ea316b8ea",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestPerformerTypeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "performer_type_coding"
    transformer = ServiceRequestPerformerTypeCodingTransformer
    expected_table_name = "service_request_performer_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
