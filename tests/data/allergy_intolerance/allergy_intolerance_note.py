"""
Test helper class for FHIR resource type AllergyIntolerance subtype note
"""

from radiant_fhir_transform_cli.transform.classes import (
    AllergyIntoleranceNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance import RESOURCE

EXPECTED_OUTPUT = [
    {
        "allergy_intolerance_id": "example_ai",
        "note_text": "The criticality is high becasue of the observed anaphylactic reaction when challenged with cashew extract.",
        "note_author_string": "Doctor J",
        "note_author_reference_reference": None,
        "note_author_reference_display": None,
        "note_author_reference_type": None,
        "note_time": "2014-02-14",
    },
]


class AllergyIntoleranceNoteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'AllergyIntolerance' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'AllergyIntolerance' resource.

    It predefines the resource type as 'AllergyIntolerance'
    and initializes the resource with the specific 'AllergyIntolerance' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'AllergyIntolerance'.

        resource (dict): The raw FHIR 'AllergyIntolerance' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'AllergyIntolerance' resource payload.
    """

    resource_type = "AllergyIntolerance"
    resource_subtype = "note"
    transformer = AllergyIntoleranceNoteTransformer
    expected_table_name = "allergy_intolerance_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
