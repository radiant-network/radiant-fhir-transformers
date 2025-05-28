"""
FHIR Procedure InstantiatesCanonical transformer
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
            "procedure_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "instantiatesCanonical",
        "columns": {
            "instantiates_canonical": {"type": "str"},
        },
    },
]


class ProcedureInstantiatesCanonicalTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'instantiatesCanonical' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'instantiatesCanonical' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('instantiates_canonical').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureInstantiatesCanonicalTransformer instance with the resource type 'Procedure',
            subtype 'instantiates_canonical', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Procedure", "instantiates_canonical", TRANSFORM_SCHEMA
        )
