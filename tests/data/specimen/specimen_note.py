"""
Test helper class for FHIR resource type Specimen subtype note
"""

from radiant_fhir_transform_cli.transform.classes import (
    SpecimenNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen import RESOURCE

EXPECTED_OUTPUT = [
    {
        "specimen_id": "101",
        "note_text": "Specimen is grossly lipemic",
        "note_author_string": "Doctor Judy",
        "note_author_reference_reference": None,
        "note_author_reference_display": None,
        "note_time": "2011-03-01T07:03:00Z",
    },
]


class SpecimenNoteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Specimen' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Specimen' resource.

    It predefines the resource type as 'Specimen'
    and initializes the resource with the specific 'Specimen' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Specimen'.

        resource (dict): The raw FHIR 'Specimen' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Specimen' resource payload.
    """

    resource_type = "Specimen"
    resource_subtype = "note"
    transformer = SpecimenNoteTransformer
    expected_table_name = "specimen_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
