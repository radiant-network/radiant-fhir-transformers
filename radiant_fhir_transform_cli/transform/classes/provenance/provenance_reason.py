"""
FHIR Provenance Reason transformer
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
            "provenance_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "reason",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "reason_coding": {"fhir_key": "coding", "type": "str"},
            "reason_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ProvenanceReasonTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR, focusing on the 'reason' element.

    This class transforms FHIR Provenance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reason' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Provenance').
        subtype (str): Specifies the sub-element of the resource to focus on ('reason').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProvenanceReasonTransformer instance with the resource type 'Provenance',
            subtype 'reason', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", "reason", TRANSFORM_SCHEMA)
