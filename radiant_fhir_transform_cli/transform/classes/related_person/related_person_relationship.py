"""
FHIR RelatedPerson Relationship transformer
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
        "fhir_path": "relationship",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "relationship_coding": {"fhir_key": "coding", "type": "str"},
            "relationship_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class RelatedPersonRelationshipTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RelatedPerson' resource in FHIR, focusing on the 'relationship' element.

    This class transforms FHIR RelatedPerson JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'relationship' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RelatedPerson').
        subtype (str): Specifies the sub-element of the resource to focus on ('relationship').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RelatedPersonRelationshipTransformer instance with the resource type 'RelatedPerson',
            subtype 'relationship', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RelatedPerson", "relationship", TRANSFORM_SCHEMA)
