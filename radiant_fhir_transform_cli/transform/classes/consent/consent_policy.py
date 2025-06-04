"""
FHIR Consent Policy transformer
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
        "fhir_path": "policy",
        "columns": {
            "policy_authority": {"fhir_key": "authority", "type": "str"},
            "policy_uri": {"fhir_key": "uri", "type": "str"},
        },
    },
]


class ConsentPolicyTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'policy' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'policy' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('policy').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentPolicyTransformer instance with the resource type 'Consent',
            subtype 'policy', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "policy", TRANSFORM_SCHEMA)
