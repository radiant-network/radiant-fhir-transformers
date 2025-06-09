""" 
Fhir Encounter Type Class
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
        "fhir_path": "type",
        "columns": {
            "type_coding": {"fhir_key": "coding", "type": "str"},
            # TODO: Add support for nested coding fields
            "type_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class EncounterTypeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR, focusing on the 'type' element.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'type' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Encounter').
        subtype (str): Specifies the sub-element of the resource to focus on ('type').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
    __init__():
        Initializes the EncounterTypeTransformer instance with the resource type 'Encounter',
        subtype 'type', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Encounter", "type", TRANSFORM_SCHEMA)
