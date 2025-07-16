"""
FHIR BodyStructure transformer
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
        "fhir_path": "active",
        "columns": {"active": {"fhir_key": "active", "type": "bool"}},
    },
    {
        "fhir_path": "morphology",
        "columns": {"morphology_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "location",
        "columns": {"location_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "description",
        "columns": {"description": {"fhir_key": "description", "type": "str"}},
    },
    {
        "fhir_path": "patient",
        "fhir_reference": "patient_reference",
        "columns": {
            "patient_reference": {"fhir_key": "reference", "type": "str"},
            "patient_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class BodyStructureTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'BodyStructure' resource in FHIR.

    Transform BodyStructure JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the BodyStructureTransformer instance with the resource
            type 'BodyStructure' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("BodyStructure", None, TRANSFORM_SCHEMA)
