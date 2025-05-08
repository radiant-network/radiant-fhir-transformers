"""
FHIR ServiceRequest transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"type": "str"}
        },
    },
    {
        "fhir_path": "text.status",
        "columns": {
            "text_status": {"type": "str"}
        },
    },
    {
        "fhir_path": "status",
        "columns": {
            "status": { "type": "str"}
        },
    },
    {
        "fhir_path": "intent",
        "columns": {
            "intent": {"fhir_key": "intent", "type": "str"}
        },
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "occurrenceDateTime",
        "columns": {
            "occurence_date_time": {"fhir_key": "occurrenceDateTime", "type": "str"}
        },
    },
    {
        "fhir_path": "requester",
        "fhir_reference": "requester_reference",
        "columns": {
            "requester_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "requester_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ServiceRequestTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'ServiceRequest' resource in FHIR.

    Transform ServiceRequest JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ServiceRequestTransformer instance with the resource
            type 'ServiceRequest' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", None, TRANSFORM_SCHEMA)