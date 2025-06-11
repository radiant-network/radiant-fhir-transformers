"""
FHIR BodyStructure Image transformer
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
        "fhir_path": " image",
        "columns": {
            "image_content_type": {"fhir_key": "contentType", "type": "str"},
            "image_language": {"fhir_key": "language", "type": "str"},
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "image_data": {"fhir_key": "data", "type": "str"},
            "image_url": {"fhir_key": "url", "type": "str"},
            "image_size": {"fhir_key": "size", "type": "int"},
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "image_hash": {"fhir_key": "hash", "type": "str"},
            "image_title": {"fhir_key": "title", "type": "str"},
            "image_creation": {"fhir_key": "creation", "type": "datetime"},
        },
    },
]


class BodyStructureImageTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'BodyStructure' resource in FHIR, focusing on the 'image' element.

    This class transforms FHIR BodyStructure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'image' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('BodyStructure').
        subtype (str): Specifies the sub-element of the resource to focus on ('image').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the BodyStructureImageTransformer instance with the resource type 'BodyStructure',
            subtype 'image', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("BodyStructure", "image", TRANSFORM_SCHEMA)
