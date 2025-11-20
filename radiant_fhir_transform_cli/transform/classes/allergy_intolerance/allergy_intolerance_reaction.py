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
            "forEach": "reaction",
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
                    "forEach": "substance.coding",
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
                    "forEach": "manifestation",
                    "column": [
                        {
                            "name": "reaction_manifestation",
                            "path": "$this",
                            "type": "string",
                        },
                    ],
                },
                {
                    "forEach": "exposureRoute.coding",
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
                    "forEach": "note",
                    "column": [
                        {
                            "name": "reaction_note",
                            "path": "$this",
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
