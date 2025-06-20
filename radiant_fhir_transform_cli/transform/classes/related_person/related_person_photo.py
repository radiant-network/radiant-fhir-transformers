"""
FHIR RelatedPerson Photo transformer
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
            "related_person_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": " photo",
        "columns": {
            "photo_content_type": {"fhir_key": "contentType", "type": "str"},
            "photo_language": {"fhir_key": "language", "type": "str"},
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "photo_data": {"fhir_key": "data", "type": "str"},
            "photo_url": {"fhir_key": "url", "type": "str"},
            "photo_size": {"fhir_key": "size", "type": "int"},
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "photo_hash": {"fhir_key": "hash", "type": "str"},
            "photo_title": {"fhir_key": "title", "type": "str"},
            "photo_creation": {"fhir_key": "creation", "type": "datetime"},
        },
    },
]


class RelatedPersonPhotoTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RelatedPerson' resource in FHIR, focusing on the 'photo' element.

    This class transforms FHIR RelatedPerson JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'photo' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RelatedPerson').
        subtype (str): Specifies the sub-element of the resource to focus on ('photo').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RelatedPersonPhotoTransformer instance with the resource type 'RelatedPerson',
            subtype 'photo', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RelatedPerson", "photo", TRANSFORM_SCHEMA)
