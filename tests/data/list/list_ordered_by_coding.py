"""
Test helper class for FHIR resource type List subtype OrderedBy Coding
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListOrderedByCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "list_id": "med-list",
        "ordered_by_coding_system": "http://terminology.hl7.org/CodeSystem/list-order",
        "ordered_by_coding_code": "entry-date",
        "ordered_by_coding_display": None,
    }
]


class ListOrderedByCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "ordered_by_coding"
    transformer = ListOrderedByCodingTransformer
    expected_table_name = "list_ordered_by_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
