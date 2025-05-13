"""
FHIR Specimen Type Coding transformer
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
            "specimen_id": { "type": "str"},
        },
    },
    {
        "fhir_path": "type.coding",
        "columns": {
            "type_coding_system": {"fhir_key": "system", "type": "str"},
            "type_coding_code": {"fhir_key": "code", "type": "str"},
            "type_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class SpecimenTypeCodingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'type.coding' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'category.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('type.coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenTypeCodingTransformer instance with the resource type 'Specimen',
            subtype 'type.coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", "type_coding", TRANSFORM_SCHEMA)
