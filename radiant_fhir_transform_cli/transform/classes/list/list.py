"""
FHIR List transformer
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
        "fhir_path": "status",
        "columns": {
            "status": {"fhir_key": "status", "type": "str"},
        },
    },
    {
        "fhir_path": "mode",
        "columns": {
            "mode": {"fhir_key": "mode", "type": "str"},
        },
    },
    {
        "fhir_path": "title",
        "columns": {
            "title": {"fhir_key": "title", "type": "str"},
        },
    },
    {
        "fhir_path": "code",
        "columns": {
            "code_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "reference_type": "subject_type",
        "columns": {
            "subject_reference": {"fhir_key": "reference", "type": "str"},
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {"fhir_key": "reference", "type": "str"},
            "encounter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "date",
        "columns": {
            "date": {"fhir_key": "date", "type": "datetime"},
        },
    },
    {
        "fhir_path": "source",
        "fhir_reference": "source_reference",
        "columns": {
            "source_reference": {"fhir_key": "reference", "type": "str"},
            "source_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "orderedBy",
        "columns": {
            "ordered_by_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "emptyReason",
        "columns": {
            "empty_reason_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ListTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'List' resource in FHIR.

    Transform List JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ListTransformer instance with the resource
            type 'List' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("List", None, TRANSFORM_SCHEMA)
