"""
Test helper class for FHIR resource type Encounter subtype EpisodeOfCare
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_episode_of_care import (
    EncounterEpisodeOfCareTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "episode_of_care_reference": "EpisodeOfCare/example",
        "episode_of_care_type": None,
        "episode_of_care_display": None,
    }
]


class EncounterEpisodeOfCareTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource.

    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.

        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'episode_of_care'.

        transformer (class): The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the table where the transformed data is expected to be stored.
    """

    resource_type = "Encounter"
    resource_subtype = "episode_of_care"
    transformer = EncounterEpisodeOfCareTransformer
    expected_table_name = "encounter_episode_of_care"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
