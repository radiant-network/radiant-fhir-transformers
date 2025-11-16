"""FHIR CareTeam reason_code transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CareTeam",
    "name": "care_team_reason_code",
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
            "forEach": "reasonCode",
            "column": [
                {
                    "name": "reason_code_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {"name": "reason_code_text", "path": "text", "type": "string"},
            ],
        },
    ],
}


class CareTeamReasonCodeTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CareTeam", "reason_code", VIEW_DEFINITION)
