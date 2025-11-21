"""
Test helper class for FHIR resource type List subtype Note
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "note_author_reference_reference": None,
        "note_author_reference_type": None,
        "note_author_reference_display": None,
        "note_author_string": None,
        "note_time": None,
        "note_text": "Both parents, both brothers and both children (twin) are still alive.",
        "id": "7f99de97-7b3c-443f-928c-0224c06f7ba6",
        "list_id": "med-list",
    },
]


class ListNoteTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "note"
    transformer = ListNoteTransformer
    expected_table_name = "list_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
