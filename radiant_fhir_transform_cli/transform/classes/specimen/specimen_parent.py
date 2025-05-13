"""
FHIR Specimen Parent transformer
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
            "specimen_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "parent",
        "fhir_reference": "parent_reference",
        "columns": {
            "parent_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "parent_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class SpecimenParentTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'parent' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'extension' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('parent').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenRequestTransformer instance with the resource type 'Specimen',
            subtype 'parent', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", "parent", TRANSFORM_SCHEMA)
