"""
Test helper class for FHIR resource type List subtype Entry
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListEntryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "entry_flag_coding_system": "http://nehta.gov.au/codes/medications/changetype",
        "entry_flag_coding_code": "01",
        "entry_flag_coding_display": "Prescribed",
        "entry_flag_text": None,
        "entry_deleted": False,
        "entry_date": None,
        "entry_item_reference": "#fmh-1",
        "entry_item_type": None,
        "entry_item_display": "hydroxocobalamin",
        "id": "a82090ca-ea1c-4a57-a3c4-e50d3a3565e3",
        "list_id": "med-list",
    },
    {
        "entry_flag_coding_system": "http://nehta.gov.au/codes/medications/changetype",
        "entry_flag_coding_code": "02",
        "entry_flag_coding_display": "Cancelled",
        "entry_flag_text": None,
        "entry_deleted": True,
        "entry_date": None,
        "entry_item_reference": "#fmh-2",
        "entry_item_type": None,
        "entry_item_display": "Morphine Sulfate",
        "id": "164974aa-513a-47b4-a45a-3d17f45f0a52",
        "list_id": "med-list",
    },
]


class ListEntryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "entry"
    transformer = ListEntryTransformer
    expected_table_name = "list_entry"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
