"""FHIR Consent policy transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_policy",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "consent_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "policy",
            "column": [
                {
                    "name": "policy_authority",
                    "path": "authority",
                    "type": "string",
                },
                {"name": "policy_uri", "path": "uri", "type": "string"},
            ],
        },
    ],
}


class ConsentPolicyTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "policy", VIEW_DEFINITION)
