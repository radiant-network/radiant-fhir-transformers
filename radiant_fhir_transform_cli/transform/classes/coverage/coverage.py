"""
FHIR Coverage transformer
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
        "fhir_path": "type.text",
        "columns": {
            "type_text": {"type": "str"},
        },
    },
    {
        "fhir_path": "policyHolder",
        "fhir_reference": "policy_holder_reference",
        "columns": {
            "policy_holder_reference": {"fhir_key": "reference", "type": "str"},
            "policy_holder_type": {"fhir_key": "type", "type": "str"},
            "policy_holder_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "subscriber",
        "fhir_reference": "subscriber_reference",
        "columns": {
            "subscriber_reference": {"fhir_key": "reference", "type": "str"},
            "subscriber_type": {"fhir_key": "type", "type": "str"},
            "subscriber_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "subscriberId",
        "columns": {
            "subscriber_id": {"fhir_key": "subscriberId", "type": "str"},
        },
    },
    {
        "fhir_path": "beneficiary",
        "fhir_reference": "beneficiary_reference",
        "columns": {
            "beneficiary_reference": {"fhir_key": "reference", "type": "str"},
            "beneficiary_type": {"fhir_key": "type", "type": "str"},
            "beneficiary_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "dependent",
        "columns": {
            "dependent": {"fhir_key": "dependent", "type": "str"},
        },
    },
    {
        "fhir_path": "relationship.text",
        "columns": {
            "relationship_text": {"type": "str"},
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
        "fhir_path": "order",
        "columns": {
            "order": {"fhir_key": "order", "type": "int"},
        },
    },
    {
        "fhir_path": "network",
        "columns": {
            "network": {"fhir_key": "network", "type": "str"},
        },
    },
    {
        "fhir_path": "subrogation",
        "columns": {
            "subrogation": {"fhir_key": "subrogation", "type": "bool"},
        },
    },
]


class CoverageTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Coverage' resource in FHIR.

    Transform Coverage JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the CoverageTransformer instance with the resource
            type 'Coverage' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Coverage", None, TRANSFORM_SCHEMA)
