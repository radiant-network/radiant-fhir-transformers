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
        "allergy_intolerance_id": "example_ai",
        "reaction_substance_text": None,
        "reaction_substance_coding": [
            {
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": "1160593",
                "display": "cashew nut allergenic extract Injectable Product",
            }
        ],
        "reaction_manifestation": [
            {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "39579001",
                        "display": "Anaphylactic reaction",
                    }
                ]
            }
        ],
        "reaction_description": "Challenge Protocol. Severe reaction to subcutaneous cashew extract. Epinephrine administered",
        "reaction_onset": "2012-06-12",
        "reaction_severity": "severe",
        "reaction_exposure_route_text": None,
        "reaction_exposure_route_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "34206005",
                "display": "Subcutaneous route",
            }
        ],
        "reaction_note": None,
    },
    {
        "allergy_intolerance_id": "example_ai",
        "reaction_substance_text": None,
        "reaction_substance_coding": None,
        "reaction_manifestation": [
            {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "64305001",
                        "display": "Urticaria",
                    }
                ]
            }
        ],
        "reaction_description": None,
        "reaction_onset": "2004",
        "reaction_severity": "moderate",
        "reaction_exposure_route_text": None,
        "reaction_exposure_route_coding": None,
        "reaction_note": [
            {
                "text": "The patient reports that the onset of urticaria was within 15 minutes of eating cashews.",
                "authorString": "Doctor J",
                "time": "2014-02-14",
            }
        ],
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
