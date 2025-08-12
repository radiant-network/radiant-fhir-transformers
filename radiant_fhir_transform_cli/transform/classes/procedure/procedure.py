"""
FHIR Procedure transformer
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
            "resource_type": {"fhir_key": "resourceType", "type": "str"}
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "statusReason.text",
        "columns": {"status_reason_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "category.text",
        "columns": {"category_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "code.text",
        "columns": {"code_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
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
        "fhir_path": "performedDateTime",
        "columns": {
            "performed_date_time": {
                "fhir_key": "performedDateTime",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "performedPeriod",
        "columns": {
            "performed_period_start": {"fhir_key": "start", "type": "datetime"},
            "performed_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "performedString",
        "columns": {
            "performed_string": {"fhir_key": "performedString", "type": "str"},
        },
    },
    {
        "fhir_path": "performedAge",
        "columns": {
            "performed_age_value": {"fhir_key": "value", "type": "str"},
            "performed_age_unit": {"fhir_key": "unit", "type": "str"},
            "performed_age_system": {"fhir_key": "system", "type": "str"},
            "performed_age_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "performedRange",
        "columns": {
            "performed_range_low_value": {
                "fhir_key": "low.value",
                "type": "str",
            },
            "performed_range_low_unit": {"fhir_key": "low.unit", "type": "str"},
            "performed_range_low_system": {
                "fhir_key": "low.system",
                "type": "str",
            },
            "performed_range_low_code": {"fhir_key": "low.code", "type": "str"},
            "performed_range_high_value": {
                "fhir_key": "high.value",
                "type": "str",
            },
            "performed_range_high_unit": {
                "fhir_key": "high.unit",
                "type": "str",
            },
            "performed_range_high_system": {
                "fhir_key": "high.system",
                "type": "str",
            },
            "performed_range_high_code": {
                "fhir_key": "high.code",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "recorder",
        "fhir_reference": "recorder_reference",
        "columns": {
            "recorder_reference": {"fhir_key": "reference", "type": "str"},
            "recorder_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "asserter",
        "fhir_reference": "asserter_reference",
        "columns": {
            "asserter_reference": {"fhir_key": "reference", "type": "str"},
            "asserter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "location",
        "fhir_reference": "location_reference",
        "columns": {
            "location_reference": {"fhir_key": "reference", "type": "str"},
            "location_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "outcome.text",
        "columns": {"outcome_text": {"fhir_key": "text", "type": "str"}},
    },
]


class ProcedureTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR.

    Transform Procedure JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ProcedureTransformer instance with the resource
            type 'Procedure' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", None, TRANSFORM_SCHEMA)
