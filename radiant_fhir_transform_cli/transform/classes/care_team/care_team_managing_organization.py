"""FHIR CareTeam managing_organization transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "CareTeam",
    "name": "care_team_managing_organization",
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
                    "name": "care_team_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "managingOrganization",
            "column": [
                {
                    "name": "managing_organization_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "managing_organization_type",
                    "path": "type",
                    "type": "string",
                },
                {
                    "name": "managing_organization_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class CareTeamManagingOrganizationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("CareTeam", "managing_organization", VIEW_DEFINITION)
