"""FHIR CareTeam telecom transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "CareTeam",
    "name": "care_team_telecom",
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
                    "name": "care_team_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "telecom",
            "column": [
                {
                    "name": "telecom_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "telecom_value",
                    "path": "value",
                    "type": "string",
                },
                {
                    "name": "telecom_use",
                    "path": "use",
                    "type": "string",
                },
                {
                    "name": "telecom_rank",
                    "path": "rank",
                    "type": "integer",
                },
                {
                    "name": "telecom_period_start",
                    "path": "period.start",
                    "type": "dateTime",
                },
                {
                    "name": "telecom_period_end",
                    "path": "period.end",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class CareTeamTelecomTransformer(FhirResourceTransformer):
    resource_type = "CareTeam"
    resource_component = "telecom"
    view_definition = VIEW_DEFINITION
