"""
Test helper class for FHIR resource type List subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "list_id": "med-list",
        "code_coding_system": "http://snomed.info/sct",
        "code_coding_code": "182836005",
        "code_coding_display": "Review of medication",
    }
]


class ListCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = ListCodeCodingTransformer
    expected_table_name = "list_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
