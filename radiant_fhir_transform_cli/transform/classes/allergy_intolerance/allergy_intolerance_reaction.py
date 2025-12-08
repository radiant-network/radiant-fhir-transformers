"""FHIR AllergyIntolerance reaction transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "AllergyIntolerance",
    "name": "allergy_intolerance_reaction",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "allergy_intolerance_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "reaction",
            "column": [
                {
                    "name": "reaction_substance_text",
                    "path": "substance.text",
                    "type": "string",
                },
                {
                    "name": "reaction_description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "reaction_onset",
                    "path": "onset",
                    "type": "dateTime",
                },
                {
                    "name": "reaction_severity",
                    "path": "severity",
                    "type": "string",
                },
                {
                    "name": "reaction_exposure_route_text",
                    "path": "exposureRoute.text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "substance.coding",
                    "column": [
                        {
                            "name": "reaction_substance_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "reaction_substance_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "reaction_substance_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "manifestation",
                    "column": [
                        {
                            "name": "reaction_manifestation_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "reaction_manifestation_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "reaction_manifestation_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "exposureRoute.coding",
                    "column": [
                        {
                            "name": "reaction_exposure_route_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "reaction_exposure_route_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "reaction_exposure_route_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEachOrNull": "note",
                    "column": [
                        {
                            "name": "reaction_note_text",
                            "path": "text",
                            "type": "string",
                        },
                        {
                            "name": "reaction_note_author_string",
                            "path": "authorString",
                            "type": "string",
                        },
                        {
                            "name": "reaction_note_time",
                            "path": "time",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class AllergyIntoleranceReactionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("AllergyIntolerance", "reaction", VIEW_DEFINITION)
