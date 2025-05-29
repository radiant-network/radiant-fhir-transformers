"""
FHIR Encounter transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
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
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "class",
        "columns": {
            "class_code": {"fhir_key": "code", "type": "str"},
            "class_system": {"fhir_key": "system", "type": "str"},
            "class_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "priority.text",
        "columns": {"priority_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {"fhir_key": "reference", "type": "str"},
            "subject_type": {"fhir_key": "type", "type": "str"},
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "period",
        "columns": {
            "period_start": {"fhir_key": "start", "type": "datetime"},
            "period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "length",
        "columns": {
            "length_value": {"fhir_key": "value", "type": "str"},
            "length_comparator": {"fhir_key": "comparator", "type": "str"},
            "length_unit": {"fhir_key": "unit", "type": "str"},
            "length_system": {"fhir_key": "system", "type": "str"},
            "length_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "serviceProvider",
        "fhir_reference": "service_provider_reference",
        "columns": {
            "service_provider_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "service_provider_type": {"fhir_key": "type", "type": "str"},
            "service_provider_display": {"fhir_key": "display", "type": "str"},
        },
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


class EncounterTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' resource in FHIR.

    Transform Encounter JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the EncounterTransformer instance with the resource
            type 'Encounter' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Encounter", None, TRANSFORM_SCHEMA)
