"""
FHIR Provenance transformer
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
        "fhir_path": "occurredPeriod",
        "columns": {
            "occurred_period_start": {"fhir_key": "start", "type": "datetime"},
            "occurred_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "occurredDateTime",
        "columns": {
            "occurred_date_time": {
                "fhir_key": "occurredDateTime",
                "type": "datetime",
            }
        },
    },
    {
        "fhir_path": "recorded",
        "columns": {
            "recorded": {"fhir_key": "recorded", "type": "datetime"},
        },
    },
    {
        "fhir_path": "location",
        "fhir_reference": "location_reference",
        "columns": {
            "location_reference": {"fhir_key": "reference", "type": "str"},
            "location_type": {"fhir_key": "type", "type": "str"},
            "location_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "activity",
        "columns": {
            "activity_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ProvenanceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Provenance' resource in FHIR.

    Transform Provenance JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ProvenanceTransformer instance with the resource
            type 'Provenance' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Provenance", None, TRANSFORM_SCHEMA)
