"""
FHIR Consent Provision Class transformer
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
        "fhir_path": "provision.class",
        "columns": {
            "provision_class_system": {"fhir_key": "system", "type": "str"},
            "provision_class_code": {"fhir_key": "code", "type": "str"},
            "provision_class_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ConsentProvisionClassTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'provision.class' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'provision.class' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('provision_class').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentProvisionClassTransformer instance with the resource type 'Consent',
            subtype 'provision_class', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "provision_class", TRANSFORM_SCHEMA)
