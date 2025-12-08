"""
Test helper class for FHIR resource type Condition subtype Note
"""

from radiant_fhir_transform_cli.transform.classes.condition import (
    ConditionNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "note_text": "This is a test note for the condition.",
        "note_time": None,
        "note_author_reference_reference": None,
        "note_author_reference_display": None,
        "note_author_reference_type": None,
        "note_author_string": None,
        "id": "9dbd5112-f621-4d0b-90bd-a990409cbc24",
        "condition_id": "f201",
    },
]


class ConditionNoteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Condition' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Condition' resource.

    It predefines the resource type as 'Condition'
    and initializes the resource with the specific 'Condition' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Condition'.

        resource_subtype (str): The subtype of the FHIR resource being tested, which
          is set to 'note'.

        transformer: The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the expected output table.
    """

    resource_type = "Condition"
    resource_subtype = "note"
    transformer = ConditionNoteTransformer
    expected_table_name = "condition_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
