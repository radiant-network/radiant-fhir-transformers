"""
FHIR Specimen Request transformer
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
            "specimen_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "request",
        "fhir_reference": "request_reference",
        "columns": {
            "request_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "request_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class SpecimenRequestTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'request' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'extension' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('request').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenRequestTransformer instance with the resource type 'Specimen',
            subtype 'request', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", "request", TRANSFORM_SCHEMA)
