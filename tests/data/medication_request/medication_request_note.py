"""
Test helper class for FHIR resource type MedicationRequest subtype Note
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "note_author_reference_reference": None,
        "note_author_reference_type": None,
        "note_author_reference_display": None,
        "note_author_string": None,
        "note_time": None,
        "note_text": "Patient told to take with food",
        "id": "9b9a09fe-0c09-4751-91fa-f3990510b947",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestNoteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'MedicationRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationRequest' resource.

    It predefines the resource type as 'MedicationRequest'
    and initializes the resource with the specific 'MedicationRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationRequest'.

        resource (dict): The raw FHIR 'MedicationRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationRequest' resource payload.
    """

    resource_type = "MedicationRequest"
    resource_subtype = "note"
    transformer = MedicationRequestNoteTransformer
    expected_table_name = "medication_request_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
