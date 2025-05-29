"""
FHIR AllergyIntolerance Category transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "allergy_intolerance_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "category",
        "columns": {
            "category": {"type": "str"},
        },
    },
]


class AllergyIntoleranceCategoryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'AllergyIntolerance' resource in FHIR, focusing on the 'category' element.
    This class transforms FHIR AllergyIntolerance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'category' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('AllergyIntolerance').
        subtype (str): Specifies the sub-element of the resource to focus on ('category').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the AllergyIntoleranceCategoryTransformer instance with the resource type 'AllergyIntolerance',
            subtype 'category', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("AllergyIntolerance", "category", TRANSFORM_SCHEMA)
