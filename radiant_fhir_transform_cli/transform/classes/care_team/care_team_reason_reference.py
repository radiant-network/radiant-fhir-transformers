"""FHIR CareTeam reason_reference transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "CareTeam",
    "name": "care_team_reason_reference",
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
            "forEachOrNull": "reasonReference",
            "column": [
                {
                    "name": "reason_reference_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "reason_reference_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "reason_reference_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class CareTeamReasonReferenceTransformer(FhirResourceTransformer):
    resource_type = "CareTeam"
    resource_component = "reason_reference"
    view_definition = VIEW_DEFINITION
