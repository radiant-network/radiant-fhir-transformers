"""
FHIR Provenance Entity transformer
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
        "fhir_path": "entity",
        "columns": {
            "entity_role": {"fhir_key": "role", "type": "str"},
            "entity_what_reference": {
                "fhir_key": "what.reference",
                "type": "str",
            },
            "entity_what_type": {"fhir_key": "what.type", "type": "str"},
            "entity_what_display": {"fhir_key": "what.display", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "entity_agent": {"fhir_key": "agent", "type": "str"},
        },
    },
]


class ProvenanceEntityTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR, focusing on the 'entity' element.

    This class transforms FHIR Provenance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'entity' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Provenance').
        subtype (str): Specifies the sub-element of the resource to focus on ('entity').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProvenanceEntityTransformer instance with the resource type 'Provenance',
            subtype 'entity', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", "entity", TRANSFORM_SCHEMA)
