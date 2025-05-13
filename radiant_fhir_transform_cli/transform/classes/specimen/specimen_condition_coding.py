"""
FHIR Specimen Condition transformer
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
            "specimen_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "condition",
        "columns": {
            "condition_coding_coding": {"fhir_key": "coding", "type": "str"},
            "condition_coding_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class SpecimenConditionCodingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'condition' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'category' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('condition').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenConditionTransformer instance with the resource type 'Specimen',
            subtype 'condition', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", "condition", TRANSFORM_SCHEMA)
