"""
FHIR Observation Note transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_DICT = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "columns": {
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "note.text",
        "columns": {
            "note_text": {
                "fhir_key": "note.text",
                "type": "str",
            },
        },
    },
]


class ObservationNoteTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'note' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'extension' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('note').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationCategoryCodingTransformer instance with the resource type 'Observation',
            subtype 'note', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "note", TRANSFORM_DICT)
