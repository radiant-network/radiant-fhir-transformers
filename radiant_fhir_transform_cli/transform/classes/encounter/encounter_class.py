"""
FHIR Encounter Class transformer
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
        "fhir_path": "class",
        "columns": {
            "class_code": {"fhir_key": "code", "type": "str"},
            "class_display": {"fhir_key": "display", "type": "str"},
            "class_system": {"fhir_key": "system", "type": "str"},
        },
    },
]


class EncounterClassTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR, focusing on the 'class' element.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'class' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('class').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
    __init__():
        Initializes the EncounterClassTransformer instance with the resource type 'Encounter',
        subtype 'class', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Encounter", "class", TRANSFORM_SCHEMA)
