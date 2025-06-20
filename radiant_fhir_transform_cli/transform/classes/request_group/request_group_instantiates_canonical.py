"""
FHIR RequestGroup InstantiatesCanonical transformer
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
            "request_group_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "instantiatesCanonical",
        "columns": {
            "instantiates_canonical": {
                "fhir_key": "instantiatesCanonical",
                "type": "str",
            },
        },
    },
]


class RequestGroupInstantiatesCanonicalTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RequestGroup' resource in FHIR, focusing on the 'instantiatesCanonical' element.

    This class transforms FHIR RequestGroup JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'instantiatesCanonical' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RequestGroup').
        subtype (str): Specifies the sub-element of the resource to focus on ('instantiates_canonical').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RequestGroupInstantiatesCanonicalTransformer instance with the resource type 'RequestGroup',
            subtype 'instantiates_canonical', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "RequestGroup", "instantiates_canonical", TRANSFORM_SCHEMA
        )
