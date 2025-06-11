"""
FHIR BodyStructure Location Coding transformer
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
        "fhir_path": "location.coding",
        "columns": {
            "location_coding_system": {"fhir_key": "system", "type": "str"},
            "location_coding_code": {"fhir_key": "code", "type": "str"},
            "location_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class BodyStructureLocationCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'BodyStructure' resource in FHIR, focusing on the 'location.coding' element.

    This class transforms FHIR BodyStructure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'location.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('BodyStructure').
        subtype (str): Specifies the sub-element of the resource to focus on ('location_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the BodyStructureLocationCodingTransformer instance with the resource type 'BodyStructure',
            subtype 'location_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("BodyStructure", "location_coding", TRANSFORM_SCHEMA)
