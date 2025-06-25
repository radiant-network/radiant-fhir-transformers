"""
FHIR DocumentReference Context Event transformer
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
        "fhir_path": "context.event",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "context_event_coding": {"fhir_key": "coding", "type": "str"},
            "context_event_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class DocumentReferenceContextEventTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'context.event' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'context.event' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('context_event').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceContextEventTransformer instance with the resource type 'DocumentReference',
            subtype 'context_event', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("DocumentReference", "context_event", TRANSFORM_SCHEMA)
