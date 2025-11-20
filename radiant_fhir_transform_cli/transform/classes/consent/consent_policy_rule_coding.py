"""FHIR Consent policy_rule_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Consent",
    "name": "consent_policy_rule_coding",
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
                    "name": "consent_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "policyRule.coding",
            "column": [
                {
                    "name": "policy_rule_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "policy_rule_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "policy_rule_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConsentPolicyRuleCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Consent", "policy_rule_coding", VIEW_DEFINITION)
