"""
FHIR Consent Provision SecurityLabel transformer
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
        "fhir_path": "provision.securityLabel",
        "columns": {
            "provision_security_label_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "provision_security_label_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "provision_security_label_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ConsentProvisionSecurityLabelTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'provision.securityLabel' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'provision.securityLabel' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('provision_security_label').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentProvisionSecurityLabelTransformer instance with the resource type 'Consent',
            subtype 'provision_security_label', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Consent", "provision_security_label", TRANSFORM_SCHEMA
        )
