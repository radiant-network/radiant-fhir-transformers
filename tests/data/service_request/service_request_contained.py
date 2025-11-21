"""
Test helper class for FHIR resource type ServiceRequest subtype contained
"""

from radiant_fhir_transform_cli.transform.classes import (
    ServiceRequestContainedTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .service_request import RESOURCE

EXPECTED_OUTPUT = [
    {
        "contained_resource_type": "Observation",
        "contained_id": "fasting",
        "contained_status": "final",
        "contained_code_text": None,
        "contained_subject_reference": "Patient/example",
        "contained_subject_display": None,
        "contained_subject_type": None,
        "contained_collection_collected_date_time": None,
        "id": "390b8ddc-cd05-4b7e-9fbd-3f82cd116d89",
        "service_request_id": "di_abcd_efg",
    },
    {
        "contained_resource_type": "Specimen",
        "contained_id": "serum",
        "contained_status": None,
        "contained_code_text": None,
        "contained_subject_reference": "Patient/example",
        "contained_subject_display": None,
        "contained_subject_type": None,
        "contained_collection_collected_date_time": "2015-08-16T06:40:17Z",
        "id": "23155e43-3b76-490f-bd1c-01306f7c6a96",
        "service_request_id": "di_abcd_efg",
    },
]


class ServiceRequestContainedTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "contained"
    transformer = ServiceRequestContainedTransformer
    expected_table_name = "service_request_contained"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
