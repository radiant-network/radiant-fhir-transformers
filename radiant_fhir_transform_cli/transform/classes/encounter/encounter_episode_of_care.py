"""
Fhir Encounter Episode of Care Class
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "encounter_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "episodeOfCare",
        "columns": {
            "episode_of_care_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "episode_of_care_type": {"fhir_key": "type", "type": "str"},
            "episode_of_care_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class EncounterEpisodeOfCareTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR, focusing on the 'episodeOfCare' element.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'episodeOfCare' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('episode_of_care').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    """

    def __init__(self):
        super().__init__("Encounter", "episode_of_care", TRANSFORM_SCHEMA)
