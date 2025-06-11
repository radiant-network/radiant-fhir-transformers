"""
FHIR BodyStructure LocationQualifier transformer
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
        "fhir_path": "locationQualifier",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "location_qualifier_coding": {"fhir_key": "coding", "type": "str"},
            "location_qualifier_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class BodyStructureLocationQualifierTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'BodyStructure' resource in FHIR, focusing on the 'locationQualifier' element.

    This class transforms FHIR BodyStructure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'locationQualifier' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('BodyStructure').
        subtype (str): Specifies the sub-element of the resource to focus on ('location_qualifier').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the BodyStructureLocationQualifierTransformer instance with the resource type 'BodyStructure',
            subtype 'location_qualifier', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "BodyStructure", "location_qualifier", TRANSFORM_SCHEMA
        )
