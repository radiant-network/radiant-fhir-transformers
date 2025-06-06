"""
FHIR Consent Verification transformer
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
        "fhir_path": "verification",
        "columns": {
            "verification_verified": {"fhir_key": "verified", "type": "bool"},
            "verification_verified_with_reference": {
                "fhir_key": "verifiedWith.reference",
                "type": "str",
            },
            "verification_verified_with_type": {
                "fhir_key": "verifiedWith.type",
                "type": "str",
            },
            "verification_verified_with_display": {
                "fhir_key": "verifiedWith.display",
                "type": "str",
            },
            "verification_verification_date": {
                "fhir_key": "verificationDate",
                "type": "datetime",
            },
        },
    },
]


class ConsentVerificationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'verification' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'verification' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('verification').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentVerificationTransformer instance with the resource type 'Consent',
            subtype 'verification', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "verification", TRANSFORM_SCHEMA)
