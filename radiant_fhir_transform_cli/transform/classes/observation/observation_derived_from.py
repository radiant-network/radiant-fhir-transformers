"""
FHIR Observation DerivedFrom transformer
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
        "fhir_path": "derivedFrom",
        "fhir_reference": "derived_from_reference",
        "columns": {
            "derived_from_reference": {"fhir_key": "reference", "type": "str"},
            "derived_from_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ObservationDerivedFromTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'derivedFrom' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'derivedFrom' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('derived_from').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationDerivedFromTransformer instance with the resource type 'Observation',
            subtype 'derived_from', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "derived_from", TRANSFORM_SCHEMA)
