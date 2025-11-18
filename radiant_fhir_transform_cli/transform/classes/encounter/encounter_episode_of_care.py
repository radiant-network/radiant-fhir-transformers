"""FHIR Encounter episode_of_care transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_episode_of_care",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "encounter_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "episodeOfCare",
            "column": [
                {
                    "name": "episode_of_care_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "episode_of_care_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "episode_of_care_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterEpisodeOfCareTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "episode_of_care", VIEW_DEFINITION)
