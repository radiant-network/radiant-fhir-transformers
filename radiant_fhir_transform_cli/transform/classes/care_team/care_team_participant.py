"""FHIR CareTeam participant transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CareTeam",
    "name": "care_team_participant",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "care_team_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "participant",
            "column": [
                {
                    "name": "participant_role_coding",
                    "path": "role.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "participant_role_text",
                    "path": "role.text",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "participant_member_reference",
                    "path": "member.reference",
                    "type": "string",
                },
                {
                    "name": "participant_member_type",
                    "path": "member.type",
                    "type": "string",
                },
                {
                    "name": "participant_member_display",
                    "path": "member.display",
                    "type": "string",
                },
                {
                    "name": "participant_on_behalf_of_reference",
                    "path": "onBehalfOf.reference",
                    "type": "string",
                },
                {
                    "name": "participant_on_behalf_of_type",
                    "path": "onBehalfOf.type",
                    "type": "string",
                },
                {
                    "name": "participant_on_behalf_of_display",
                    "path": "onBehalfOf.display",
                    "type": "string",
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
            ],
        },
    ],
}


class CareTeamParticipantTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CareTeam", "participant", VIEW_DEFINITION)
