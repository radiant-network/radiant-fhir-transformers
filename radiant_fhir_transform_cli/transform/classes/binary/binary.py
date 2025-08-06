"""
FHIR Binary transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"},
        },
    },
    {
        "fhir_path": "contentType",
        "columns": {
            "content_type": {"fhir_key": "contentType", "type": "str"},
        },
    },
    {
        "fhir_path": "securityContext",
        "fhir_reference": "security_context_reference",
        "columns": {
            "security_context_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "security_context_type": {"fhir_key": "type", "type": "str"},
            "security_context_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "data",
        "columns": {
            "data": {"fhir_key": "data", "type": "str"},
        },
    },
]


class BinaryTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Binary' resource in FHIR.

    Transform Binary JSON objects into flat dictionaries representing
    rows in an output CSV file

    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the BinaryTransformer instance with the resource
            type 'Binary' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Binary", None, TRANSFORM_SCHEMA)
