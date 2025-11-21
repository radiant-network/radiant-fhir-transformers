"""
Test helper class for FHIR resource type RequestGroup subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.request_group import (
    RequestGroupCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .request_group_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://snomed.info/sct",
        "code_coding_code": "18629005",
        "code_coding_display": "Administration of drug or medicament (procedure)",
        "id": "60374ed3-120e-4776-b8f4-da186e0d1005",
        "request_group_id": "kdn5-example",
    },
]


class RequestGroupCodeCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'RequestGroup' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'RequestGroup' resource.

    It predefines the resource type as 'RequestGroup'
    and initializes the resource with the specific 'RequestGroup' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'RequestGroup'.
        resource (dict): The raw FHIR 'RequestGroup' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'RequestGroup' resource payload.
    """

    resource_type = "RequestGroup"
    resource_subtype = "code_coding"
    transformer = RequestGroupCodeCodingTransformer
    expected_table_name = "request_group_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
