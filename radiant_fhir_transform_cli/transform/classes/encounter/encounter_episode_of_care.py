"""FHIR Encounter episode_of_care transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_episode_of_care",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
                {
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "episodeOfCare",
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
    resource_type = "Encounter"
    resource_component = "episode_of_care"
    view_definition = VIEW_DEFINITION
