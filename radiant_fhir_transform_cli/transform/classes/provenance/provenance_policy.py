"""
FHIR Provenance Policy transformer
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
        "fhir_path": "policy",
        "columns": {
            "policy": {"fhir_key": "policy", "type": "str"},
        },
    },
]


class ProvenancePolicyTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR, focusing on the 'policy' element.

    This class transforms FHIR Provenance JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'policy' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Provenance').
        subtype (str): Specifies the sub-element of the resource to focus on ('policy').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProvenancePolicyTransformer instance with the resource type 'Provenance',
            subtype 'policy', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", "policy", TRANSFORM_SCHEMA)
