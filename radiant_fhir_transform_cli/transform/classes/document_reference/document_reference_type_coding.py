"""
FHIR DocumentReference Type Coding transformer
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
        "fhir_path": "type.coding",
        "columns": {
            "type_coding_system": {"fhir_key": "system", "type": "str"},
            "type_coding_code": {"fhir_key": "code", "type": "str"},
            "type_coding_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "type.text",
        "columns": {
            "type_text": {"type": "str"},
        },
    },
]


class DocumentReferenceTypeCodingTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'type.coding' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'type.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('type.coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceCategoryCodingTransformer instance with the resource type 'Observation',
            subtype 'type.coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", "type_coding", TRANSFORM_SCHEMA)
