"""
Test helper class for FHIR resource type CarePlan subtype note
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanNoteTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "note_text": "Patient family is not ready to commit to goal setting at this time.  Goal setting will be addressed in the future",
        "note_author_string": None,
        "note_author_reference_reference": None,
        "note_author_reference_display": None,
        "note_author_reference_type": None,
        "note_time": "2014-02-14",
        "id": "bfb88e5c-887c-47f5-950f-73639f6dba39",
        "care_plan_id": "preg",
    },
]


class CarePlanNoteTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'CarePlan' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'CarePlan' resource.

    It predefines the resource type as 'CarePlan'
    and initializes the resource with the specific 'CarePlan' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'CarePlan'.

        resource (dict): The raw FHIR 'CarePlan' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'CarePlan' resource payload.
    """

    resource_type = "CarePlan"
    resource_subtype = "note"
    transformer = CarePlanNoteTransformer
    expected_table_name = "care_plan_note"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
