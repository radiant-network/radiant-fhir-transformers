"""
FHIR DocumentReference Identifier transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
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
        "fhir_path": "identifier",
        "columns": {
            "identifier_system": {"fhir_key": "system", "type": "str"},
            "identifier_value": {"fhir_key": "value", "type": "str"},
        },
    },
]


class DocumentReferenceIdentifierTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'identifier' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'identifier' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('identifier').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceCategoryCodingTransformer instance with the resource type 'Observation',
            subtype 'identifier', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", "identifier", TRANSFORM_SCHEMA)
