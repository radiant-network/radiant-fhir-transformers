"""
Test helper class for FHIR resource type AllergyIntolerance subtype reaction
"""

from radiant_fhir_transform_cli.transform.classes import (
    AllergyIntoleranceReactionTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .allergy_intolerance import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reaction_note_text": None,
        "reaction_note_author_string": None,
        "reaction_note_time": None,
        "reaction_exposure_route_coding_system": "http://snomed.info/sct",
        "reaction_exposure_route_coding_code": "34206005",
        "reaction_exposure_route_coding_display": "Subcutaneous route",
        "reaction_manifestation_coding_system": None,
        "reaction_manifestation_coding_code": None,
        "reaction_manifestation_coding_display": None,
        "reaction_substance_coding_system": "http://www.nlm.nih.gov/research/umls/rxnorm",
        "reaction_substance_coding_code": "1160593",
        "reaction_substance_coding_display": "cashew nut allergenic extract Injectable Product",
        "reaction_substance_text": None,
        "reaction_description": "Challenge Protocol. Severe reaction to subcutaneous cashew extract. Epinephrine administered",
        "reaction_onset": "2012-06-12",
        "reaction_severity": "severe",
        "reaction_exposure_route_text": None,
        "id": "c3639a86-65bd-4203-8264-de350e3be625",
        "allergy_intolerance_id": "example_ai",
    },
    {
        "reaction_note_text": "The patient reports that the onset of urticaria was within 15 minutes of eating cashews.",
        "reaction_note_author_string": "Doctor J",
        "reaction_note_time": "2014-02-14",
        "reaction_exposure_route_coding_system": None,
        "reaction_exposure_route_coding_code": None,
        "reaction_exposure_route_coding_display": None,
        "reaction_manifestation_coding_system": None,
        "reaction_manifestation_coding_code": None,
        "reaction_manifestation_coding_display": None,
        "reaction_substance_coding_system": None,
        "reaction_substance_coding_code": None,
        "reaction_substance_coding_display": None,
        "reaction_substance_text": None,
        "reaction_description": None,
        "reaction_onset": "2004",
        "reaction_severity": "moderate",
        "reaction_exposure_route_text": None,
        "id": "539bd818-7de1-40c4-98f5-56a04a35a658",
        "allergy_intolerance_id": "example_ai",
    },
]


class AllergyIntoleranceReactionTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reaction"
    transformer = AllergyIntoleranceReactionTransformer
    expected_table_name = "allergy_intolerance_reaction"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
