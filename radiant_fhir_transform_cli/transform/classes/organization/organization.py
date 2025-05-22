"""
FHIR Organization transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"fhir_key": "id", "type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {
                "fhir_key": "resourceType",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "active",
        "columns": {"active": {"fhir_key": "active", "type": "bool"}},
    },
    {
        "fhir_path": "name",
        "columns": {"name": {"fhir_key": "name", "type": "str"}},
    },
    {
        "fhir_path": "partOf",
        "fhir_reference": "part_of_reference",
        "columns": {
            "part_of_reference": {"fhir_key": "reference", "type": "str"},
            "part_of_type": {"fhir_key": "type", "type": "str"},
            "part_of_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class OrganizationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Organization' resource in FHIR.

    Transform Organization JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the OrganizationTransformer instance with the resource
            type 'Organization' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Organization", None, TRANSFORM_SCHEMA)
