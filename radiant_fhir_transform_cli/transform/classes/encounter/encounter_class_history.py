"""
Fhir Encounter Class History Transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
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
            "encounter_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "classHistory",
        "columns": {
            "class_history_class": {"fhir_key": "class", "type": "str"},
            "class_history_period": {"fhir_key": "period", "type": "str"},
        },
        # TODO: Add support for nested class and period fields
    },
]


class EncounterClassHistoryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR, focusing on the 'classHistory' element.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'classHistory' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('class_history').

    Methods:
        __init__: Initializes the transformer with the resource type, subtype, and transformation schema.
    """

    def __init__(self):
        super().__init__("Encounter", "class_history", TRANSFORM_SCHEMA)
