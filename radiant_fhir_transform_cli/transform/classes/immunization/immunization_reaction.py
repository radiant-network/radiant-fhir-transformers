"""FHIR Immunization reaction transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_reaction",
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
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "reaction",
            "column": [
                {
                    "name": "reaction_date",
                    "path": "date",
                    "type": "dateTime",
                },
                {
                    "name": "reaction_detail_reference",
                    "path": "detail.reference",
                    "type": "string",
                },
                {
                    "name": "reaction_detail_type",
                    "path": "detail.type",
                    "type": "string",
                },
                {
                    "name": "reaction_detail_display",
                    "path": "detail.display",
                    "type": "string",
                },
                {
                    "name": "reaction_reported",
                    "path": "reported",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationReactionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "reaction", VIEW_DEFINITION)
