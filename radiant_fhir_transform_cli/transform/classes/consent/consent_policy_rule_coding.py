"""
FHIR Consent PolicyRule Coding transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "consent_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "policyRule.coding",
        "columns": {
            "policy_rule_coding_system": {"fhir_key": "system", "type": "str"},
            "policy_rule_coding_code": {"fhir_key": "code", "type": "str"},
            "policy_rule_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ConsentPolicyRuleCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'policyRule.coding' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'policyRule.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('policy_rule_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentPolicyRuleCodingTransformer instance with the resource type 'Consent',
            subtype 'policy_rule_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "policy_rule_coding", TRANSFORM_SCHEMA)
