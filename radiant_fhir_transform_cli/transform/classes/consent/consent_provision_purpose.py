"""
FHIR Consent Provision Purpose transformer
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
        "fhir_path": "provision.purpose",
        "columns": {
            "provision_purpose_system": {"fhir_key": "system", "type": "str"},
            "provision_purpose_code": {"fhir_key": "code", "type": "str"},
            "provision_purpose_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ConsentProvisionPurposeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'provision.purpose' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'provision.purpose' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('provision_purpose').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentProvisionPurposeTransformer instance with the resource type 'Consent',
            subtype 'provision_purpose', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "provision_purpose", TRANSFORM_SCHEMA)
