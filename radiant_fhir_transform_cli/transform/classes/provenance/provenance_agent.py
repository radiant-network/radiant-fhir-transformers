"""
FHIR Provenance Agent transformer
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
        "fhir_path": "agent",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "agent_type_coding": {"fhir_key": "type.coding", "type": "str"},
            "agent_type_text": {"fhir_key": "type.text", "type": "str"},
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "agent_role": {"fhir_key": "role", "type": "str"},
            "agent_who_reference": {"fhir_key": "who.reference", "type": "str"},
            "agent_who_type": {"fhir_key": "who.type", "type": "str"},
            "agent_who_display": {"fhir_key": "who.display", "type": "str"},
            "agent_on_behalf_of_reference": {
                "fhir_key": "onBehalfOf.reference",
                "type": "str",
            },
            "agent_on_behalf_of_type": {
                "fhir_key": "onBehalfOf.type",
                "type": "str",
            },
            "agent_on_behalf_of_display": {
                "fhir_key": "onBehalfOf.display",
                "type": "str",
            },
        },
    },
]


class ProvenanceAgentTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR, focusing on the 'agent' element.

    This class transforms FHIR Provenance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'agent' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Provenance').
        subtype (str): Specifies the sub-element of the resource to focus on ('agent').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProvenanceAgentTransformer instance with the resource type 'Provenance',
            subtype 'agent', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", "agent", TRANSFORM_SCHEMA)
