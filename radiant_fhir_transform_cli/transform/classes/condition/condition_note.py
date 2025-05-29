"""
FHIR Condition Note transformer
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
            "condition_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "note",
        "columns": {
            "note_text": {"fhir_key": "text", "type": "str"},
            "note_time": {"fhir_key": "time", "type": "datetime"},
            "note_author_reference": {
                "fhir_key": "authorReference",
                "type": "str",
            },
            "note_author_string": {"fhir_key": "authorString", "type": "str"},
        },
    },
]


class ConditionNoteTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR, focusing on the 'note' element.

    This class transforms FHIR Condition JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'note' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Condition').
        subtype (str): Specifies the sub-element of the resource to focus on ('note').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ConditionNoteTransformer instance with the resource type 'Condition',
            subtype 'note', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Condition", "note", TRANSFORM_SCHEMA)
