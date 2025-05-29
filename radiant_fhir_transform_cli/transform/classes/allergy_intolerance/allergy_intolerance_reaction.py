"""
FHIR AllergyIntolerance Reaction transformer
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
            "allergy_intolerance_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "reaction",
        "columns": {
            "reaction_substance_text": {
                "fhir_key": "substance.text",
                "type": "str",
            },
            "reaction_substance_coding": {
                "fhir_key": "substance.coding",
                "type": "str",
            },
            "reaction_manifestation": {
                "fhir_key": "manifestation",
                "type": "str",
            },
            "reaction_description": {"fhir_key": "description", "type": "str"},
            "reaction_onset": {"fhir_key": "onset", "type": "datetime"},
            "reaction_severity": {"fhir_key": "severity", "type": "str"},
            "reaction_exposure_route_text": {
                "fhir_key": "exposureRoute.text",
                "type": "str",
            },
            "reaction_exposure_route_coding": {
                "fhir_key": "exposureRoute.coding",
                "type": "str",
            },
            "reaction_note": {"fhir_key": "note", "type": "str"},
        },
    },
]


class AllergyIntoleranceReactionTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'AllergyIntolerance' resource in FHIR, focusing on the 'reaction' element.

    This class transforms FHIR AllergyIntolerance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'reaction' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('AllergyIntolerance').
        subtype (str): Specifies the sub-element of the resource to focus on ('reaction').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AllergyIntoleranceReactionTransformer instance with the resource type 'AllergyIntolerance',
            subtype 'reaction', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("AllergyIntolerance", "reaction", TRANSFORM_SCHEMA)
