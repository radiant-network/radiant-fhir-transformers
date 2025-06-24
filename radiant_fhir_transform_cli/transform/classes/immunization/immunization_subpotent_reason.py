"""
FHIR Immunization SubpotentReason transformer
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
            "immunization_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "subpotentReason",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "subpotent_reason_coding": {"fhir_key": "coding", "type": "str"},
            "subpotent_reason_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ImmunizationSubpotentReasonTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'subpotentReason' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'subpotentReason' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('subpotent_reason').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationSubpotentReasonTransformer instance with the resource type 'Immunization',
            subtype 'subpotent_reason', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", "subpotent_reason", TRANSFORM_SCHEMA)
