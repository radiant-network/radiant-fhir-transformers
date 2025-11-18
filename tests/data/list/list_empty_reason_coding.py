"""
Test helper class for FHIR resource type List subtype EmptyReason Coding
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListEmptyReasonCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "list_id": "med-list",
        "empty_reason_coding_system": "http://terminology.hl7.org/CodeSystem/list-empty-reason",
        "empty_reason_coding_code": "nilknown",
        "empty_reason_coding_display": "Nil Known",
    }
]


class ListEmptyReasonCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'List' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'List' resource.

    It predefines the resource type as 'List'
    and initializes the resource with the specific 'List' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'List'.
        resource (dict): The raw FHIR 'List' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'List' resource payload.
    """

    resource_type = "List"
    resource_subtype = "empty_reason_coding"
    transformer = ListEmptyReasonCodingTransformer
    expected_table_name = "list_empty_reason_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
