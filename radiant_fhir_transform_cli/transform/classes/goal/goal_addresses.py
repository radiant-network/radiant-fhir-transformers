"""
FHIR Goal Addresses transformer
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
            "goal_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "addresses",
        "fhir_reference": "addresses_reference",
        "columns": {
            "addresses_reference": {"fhir_key": "reference", "type": "str"},
            "addresses_type": {"fhir_key": "type", "type": "str"},
            "addresses_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class GoalAddressesTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR, focusing on the 'addresses' element.

    This class transforms FHIR Goal JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'addresses' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Goal').
        subtype (str): Specifies the sub-element of the resource to focus on ('addresses').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the GoalAddressesTransformer instance with the resource type 'Goal',
            subtype 'addresses', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", "addresses", TRANSFORM_SCHEMA)
