"""
FHIR Coverage Class transformer
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
            "coverage_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "class",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "class_type_coding": {"fhir_key": "type.coding", "type": "str"},
            "class_type_text": {"fhir_key": "type.text", "type": "str"},
            "class_value": {"fhir_key": "value", "type": "str"},
            "class_name": {"fhir_key": "name", "type": "str"},
        },
    },
]


class CoverageClassTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Coverage' resource in FHIR, focusing on the 'class' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'class' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Coverage').
        subtype (str): Specifies the sub-element of the resource to focus on ('class').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CoverageClassTransformer instance with the resource type 'Coverage',
            subtype 'class', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Coverage", "class", TRANSFORM_SCHEMA)
