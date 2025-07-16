"""
FHIR DiagnosticReport transformer
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
        "columns": {"resource_type": {"type": "str"}},
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"type": "str"}},
    },
    {
        "fhir_path": "code.text",
        "columns": {"code_text": {"type": "str"}},
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
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "encounter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "effectiveDateTime",
        "columns": {"effective_date_time": {"type": "datetime"}},
    },
    {
        "fhir_path": "effectivePeriod.start",
        "columns": {"effective_period_start": {"type": "datetime"}},
    },
    {
        "fhir_path": "effectivePeriod.stop",
        "columns": {"effective_period_stop": {"type": "datetime"}},
    },
    {
        "fhir_path": "issued",
        "columns": {"issued": {"type": "datetime"}},
    },
    {
        "fhir_path": "conclusion",
        "columns": {"conclusion": {"type": "datetime"}},
    },
]


class DiagnosticReportTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'DiagnosticReport' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the DiagnosticReportTransformer instance with the resource
            type 'DiagnosticReport' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("DiagnosticReport", None, TRANSFORM_SCHEMA)
