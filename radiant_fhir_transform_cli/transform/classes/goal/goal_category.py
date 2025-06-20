"""
FHIR Goal Category transformer
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
        "fhir_path": "category",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "category_coding": {"fhir_key": "coding", "type": "str"},
            "category_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class GoalCategoryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR, focusing on the 'category' element.

    This class transforms FHIR Goal JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'category' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Goal').
        subtype (str): Specifies the sub-element of the resource to focus on ('category').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the GoalCategoryTransformer instance with the resource type 'Goal',
            subtype 'category', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", "category", TRANSFORM_SCHEMA)
