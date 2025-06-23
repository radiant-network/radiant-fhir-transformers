"""
FHIR Immunization Performer transformer
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
        "fhir_path": "performer",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "performer_function_coding": {
                "fhir_key": "function.coding",
                "type": "str",
            },
            "performer_function_text": {
                "fhir_key": "function.text",
                "type": "str",
            },
            "performer_actor_reference": {
                "fhir_key": "actor.reference",
                "type": "str",
            },
            "performer_actor_type": {"fhir_key": "actor.type", "type": "str"},
            "performer_actor_display": {
                "fhir_key": "actor.display",
                "type": "str",
            },
        },
    },
]


class ImmunizationPerformerTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'performer' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'performer' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('performer').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationPerformerTransformer instance with the resource type 'Immunization',
            subtype 'performer', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", "performer", TRANSFORM_SCHEMA)
