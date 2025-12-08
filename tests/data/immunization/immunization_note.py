"""
Test helper class for FHIR resource type Immunization subtype note
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "note_author_reference_reference": None,
        "note_author_reference_type": None,
        "note_author_reference_display": None,
        "note_author_string": None,
        "note_time": None,
        "note_text": "Notes on adminstration of vaccine",
        "id": "dff44584-3a85-4e20-b79e-3cddfc27c143",
        "immunization_id": "example",
    },
]


class ImmunizationNoteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Immunization' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Immunization' resource.

    It predefines the resource type as 'Immunization'
    and initializes the resource with the specific 'Immunization' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Immunization'.
        resource (dict): The raw FHIR 'Immunization' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Immunization' resource payload.
    """

    resource_type = "Immunization"
    resource_subtype = "note"
    transformer = ImmunizationNoteTransformer
    expected_table_name = "immunization_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
