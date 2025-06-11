"""
FHIR BodyStructure Morphology Coding transformer
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
            "body_structure_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "morphology.coding",
        "columns": {
            "morphology_coding_system": {"fhir_key": "system", "type": "str"},
            "morphology_coding_code": {"fhir_key": "code", "type": "str"},
            "morphology_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class BodyStructureMorphologyCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'BodyStructure' resource in FHIR, focusing on the 'morphology.coding' element.

    This class transforms FHIR BodyStructure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'morphology.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('BodyStructure').
        subtype (str): Specifies the sub-element of the resource to focus on ('morphology_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the BodyStructureMorphologyCodingTransformer instance with the resource type 'BodyStructure',
            subtype 'morphology_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("BodyStructure", "morphology_coding", TRANSFORM_SCHEMA)
