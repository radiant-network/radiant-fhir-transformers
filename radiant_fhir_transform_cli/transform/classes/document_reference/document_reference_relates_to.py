"""
FHIR DocumentReference RelatesTo transformer
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
        "fhir_path": "relatesTo",
        "columns": {
            "relates_to_target_code": {"fhir_key": "code", "type": "str"},
            "relates_to_target_reference": {
                "fhir_key": "target.reference",
                "type": "str",
            },
            "relates_to_target_type": {
                "fhir_key": "target.type",
                "type": "str",
            },
            "relates_to_target_display": {
                "fhir_key": "target.display",
                "type": "str",
            },
        },
    },
]


class DocumentReferenceRelatesToTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'relatesTo' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'relatesTo' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('relates_to').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceRelatesToTransformer instance with the resource type 'DocumentReference',
            subtype 'relates_to', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", "relates_to", TRANSFORM_SCHEMA)
