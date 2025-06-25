"""
FHIR DocumentReference SecurityLabel transformer
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
        "fhir_path": "securityLabel",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "security_label_coding": {"fhir_key": "coding", "type": "str"},
            "security_label_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class DocumentReferenceSecurityLabelTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DocumentReference' resource in FHIR, focusing on the 'securityLabel' element.

    This class transforms FHIR DocumentReference JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'securityLabel' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('DocumentReference').
        subtype (str): Specifies the sub-element of the resource to focus on ('security_label').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the DocumentReferenceSecurityLabelTransformer instance with the resource type 'DocumentReference',
            subtype 'security_label', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "DocumentReference", "security_label", TRANSFORM_SCHEMA
        )
