"""
FHIR Observation Interpretation transformer
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
        "fhir_path": "interpretation",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "interpretation_coding": {"fhir_key": "coding", "type": "str"},
            "interpretation_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ObservationInterpretationTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'interpretation' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'interpretation' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('interpretation').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationInterpretationTransformer instance with the resource type 'Observation',
            subtype 'interpretation', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "interpretation", TRANSFORM_SCHEMA)
