"""
FHIR Observation Category Coding transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
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
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "category.coding",
        "columns": {
            "category_coding_system": {"fhir_key": "system", "type": "str"},
            "category_coding_code": {"fhir_key": "code", "type": "str"},
            "category_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ObservationCategoryCodingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'category.coding' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'category.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('category.coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationCategoryCodingTransformer instance with the resource type 'Observation',
            subtype 'category.coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "category_coding", TRANSFORM_SCHEMA)
