"""
FHIR Consent Provision Actor transformer
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
        "fhir_path": "provision.actor",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "provision_actor_role_coding": {
                "fhir_key": "role.coding",
                "type": "str",
            },
            "provision_actor_role_text": {
                "fhir_key": "role.text",
                "type": "str",
            },
            "provision_actor_reference_reference": {
                "fhir_key": "reference.reference",
                "type": "str",
            },
            "provision_actor_reference_type": {
                "fhir_key": "reference.type",
                "type": "str",
            },
            "provision_actor_reference_display": {
                "fhir_key": "reference.display",
                "type": "str",
            },
        },
    },
]


class ConsentProvisionActorTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'provision.actor' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'provision.actor' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('provision_actor').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentProvisionActorTransformer instance with the resource type 'Consent',
            subtype 'provision_actor', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "provision_actor", TRANSFORM_SCHEMA)
