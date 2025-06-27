"""
FHIR RequestGroup transformer
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
        "fhir_path": "groupIdentifier",
        "columns": {
            "group_identifier_type_text": {
                "fhir_key": "type.text",
                "type": "str",
            },
            "group_identifier_system": {"fhir_key": "system", "type": "str"},
            "group_identifier_value": {"fhir_key": "value", "type": "str"},
            "group_identifier_period_start": {
                "fhir_key": "period.start",
                "type": "str",
            },
            "group_identifier_period_end": {
                "fhir_key": "period.end",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "status",
        "columns": {
            "status": {"fhir_key": "status", "type": "str"},
        },
    },
    {
        "fhir_path": "intent",
        "columns": {
            "intent": {"fhir_key": "intent", "type": "str"},
        },
    },
    {
        "fhir_path": "priority",
        "columns": {
            "priority": {"fhir_key": "priority", "type": "str"},
        },
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": {"type": "str"},
        },
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
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {"fhir_key": "reference", "type": "str"},
            "encounter_type": {"fhir_key": "type", "type": "str"},
            "encounter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "authoredOn",
        "columns": {
            "authored_on": {"fhir_key": "authoredOn", "type": "datetime"},
        },
    },
    {
        "fhir_path": "author",
        "fhir_reference": "author_reference",
        "columns": {
            "author_reference": {"fhir_key": "reference", "type": "str"},
            "author_type": {"fhir_key": "type", "type": "str"},
            "author_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "RequestGroup",
        "columns": {
            "request_group_raw_json": {
                "type": "str",
            }
        },
    },
]


class RequestGroupTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RequestGroup' resource in FHIR.

    Transform RequestGroup JSON objects into flat dictionaries representing
    rows in an output CSV file

    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the RequestGroupTransformer instance with the resource
            type 'RequestGroup' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("RequestGroup", None, TRANSFORM_SCHEMA)
