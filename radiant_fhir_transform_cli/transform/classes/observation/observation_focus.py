"""
FHIR Observation Focus transformer
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
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "focus",
        "fhir_reference": "focus_reference",
        "columns": {
            "focus_reference": {"fhir_key": "reference", "type": "str"},
            "focus_type": {"fhir_key": "type", "type": "str"},
            "focus_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ObservationFocusTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'focus' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'focus' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('focus').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationFocusTransformer instance with the resource type 'Observation',
            subtype 'focus', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "focus", TRANSFORM_SCHEMA)
