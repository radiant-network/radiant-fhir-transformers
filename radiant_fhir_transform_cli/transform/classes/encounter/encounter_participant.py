"""FHIR Encounter participant transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_participant",
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
            "forEach": "participant",
            "column": [
                {
                    "name": "participant_type",
                    "path": "type",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "participant_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "participant_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
                {
                    "name": "participant_individual_reference",
                    "path": "individual.reference",
                    "type": "string",
                },
                {
                    "name": "participant_individual_type",
                    "path": "individual.type",
                    "type": "string",
                },
                {
                    "name": "participant_individual_display",
                    "path": "individual.display",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterParticipantTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "participant", VIEW_DEFINITION)
