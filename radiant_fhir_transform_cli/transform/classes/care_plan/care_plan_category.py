"""
FHIR CarePlan Category transformer
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
            "care_plan_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "category",
        "columns": {
            "category_coding": {"fhir_key": "coding", "type": "str"},
            "category_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class CarePlanCategoryTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'CarePlan' resource in FHIR, focusing on the 'category' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'category' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('category').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanCategoryTransformer instance with the resource type 'CarePlan',
            subtype 'category', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "category", TRANSFORM_SCHEMA)
