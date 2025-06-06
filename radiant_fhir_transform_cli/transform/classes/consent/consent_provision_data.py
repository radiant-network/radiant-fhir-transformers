"""
FHIR Consent Provision Data transformer
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
        "fhir_path": "provision.data",
        "columns": {
            "provision_data_meaning": {"fhir_key": "meaning", "type": "str"},
            "provision_data_reference_reference": {
                "fhir_key": "reference.reference",
                "type": "str",
            },
            "provision_data_reference_type": {
                "fhir_key": "reference.type",
                "type": "str",
            },
            "provision_data_reference_display": {
                "fhir_key": "reference.display",
                "type": "str",
            },
        },
    },
]


class ConsentProvisionDataTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR, focusing on the 'provision.data' element.

    This class transforms FHIR Consent JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'provision.data' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Consent').
        subtype (str): Specifies the sub-element of the resource to focus on ('provision_data').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConsentProvisionDataTransformer instance with the resource type 'Consent',
            subtype 'provision_data', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", "provision_data", TRANSFORM_SCHEMA)
