"""
FHIR RequestGroup InstantiatesUri transformer
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
        "fhir_path": "instantiatesUri",
        "columns": {
            "instantiates_uri": {
                "fhir_key": "instantiatesUri",
                "type": "str",
            },
        },
    },
]


class RequestGroupInstantiatesUriTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RequestGroup' resource in FHIR, focusing on the 'instantiatesUri' element.

    This class transforms FHIR RequestGroup JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'instantiatesUri' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RequestGroup').
        subtype (str): Specifies the sub-element of the resource to focus on ('instantiates_uri').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RequestGroupInstantiatesUriTransformer instance with the resource type 'RequestGroup',
            subtype 'instantiates_uri', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RequestGroup", "instantiates_uri", TRANSFORM_SCHEMA)
