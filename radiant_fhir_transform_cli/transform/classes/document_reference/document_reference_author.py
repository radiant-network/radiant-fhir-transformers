"""
FHIR DocumentReference Author transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "document_reference_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "author",
        "fhir_reference": "author_reference",
        "columns": {
            "author_reference": {"fhir_key": "reference", "type": "str"},
            "author_type": {"fhir_key": "type", "type": "str"},
            "author_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class DocumentReferenceAuthorTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'author' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'author' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('author').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceAuthorTransformer instance with the resource type 'DocumentReference',
            subtype 'author', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", "author", TRANSFORM_SCHEMA)
