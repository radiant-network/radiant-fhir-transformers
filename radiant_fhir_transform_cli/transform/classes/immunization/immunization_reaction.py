"""
FHIR Immunization Reaction transformer
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
        "fhir_path": "reaction",
        "columns": {
            "reaction_date": {"fhir_key": "date", "type": "datetime"},
            "reaction_detail_reference": {
                "fhir_key": "detail.reference",
                "type": "str",
            },
            "reaction_detail_type": {"fhir_key": "detail.type", "type": "str"},
            "reaction_detail_display": {
                "fhir_key": "detail.display",
                "type": "str",
            },
            "reaction_reported": {"fhir_key": "reported", "type": "bool"},
        },
    },
]


class ImmunizationReactionTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'reaction' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reaction' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('reaction').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationReactionTransformer instance with the resource type 'Immunization',
            subtype 'reaction', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", "reaction", TRANSFORM_SCHEMA)
