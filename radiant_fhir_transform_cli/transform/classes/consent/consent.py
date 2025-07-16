"""
FHIR Consent transformer
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
        "fhir_path": "scope",
        "columns": {
            "scope_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "patient",
        "fhir_reference": "patient_reference",
        "columns": {
            "patient_reference": {"fhir_key": "reference", "type": "str"},
            "patient_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "dateTime",
        "columns": {
            "date_time": {"fhir_key": "dateTime", "type": "datetime"},
        },
    },
    {
        "fhir_path": " sourceAttachment",
        "columns": {
            "source_attachment_content_type": {
                "fhir_key": "contentType",
                "type": "str",
            },
            "source_attachment_language": {
                "fhir_key": "language",
                "type": "str",
            },
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "source_attachment_data": {"fhir_key": "data", "type": "str"},
            "source_attachment_url": {"fhir_key": "url", "type": "str"},
            "source_attachment_size": {"fhir_key": "size", "type": "int"},
            # TODO: Handling base64Binary Data Types in Transformers (See https://github.com/radiant-network/radiant-fhir-transformers/issues/53)
            # "source_attachment_hash": {"fhir_key": "hash", "type": "str"},
            "source_attachment_title": {"fhir_key": "title", "type": "str"},
            "source_attachment_creation": {
                "fhir_key": "creation",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "sourceReference",
        "fhir_reference": "source_reference_reference",
        "columns": {
            "source_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "source_reference_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "policyRule",
        "columns": {
            "policy_rule_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "provision",
        "columns": {
            "provision_type": {"fhir_key": "type", "type": "str"},
            "provision_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "provision_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
            "provision_data_period_start": {
                "fhir_key": "dataPeriod.start",
                "type": "datetime",
            },
            "provision_data_period_end": {
                "fhir_key": "dataPeriod.end",
                "type": "datetime",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "provision_provision": {"fhir_key": "provision", "type": "str"},
        },
    },
]


class ConsentTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Consent' resource in FHIR.

    Transform Consent JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ConsentTransformer instance with the resource
            type 'Consent' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Consent", None, TRANSFORM_SCHEMA)
