"""
FHIR Provenance Target transformer
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
            "provenance_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "target",
        "fhir_reference": "target_reference",
        "columns": {
            "target_reference": {"fhir_key": "reference", "type": "str"},
            "target_type": {"fhir_key": "type", "type": "str"},
            "target_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ProvenanceTargetTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR, focusing on the 'target' element.

    This class transforms FHIR Provenance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'target' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Provenance').
        subtype (str): Specifies the sub-element of the resource to focus on ('target').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProvenanceTargetTransformer instance with the resource type 'Provenance',
            subtype 'target', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", "target", TRANSFORM_SCHEMA)
