"""
FHIR AllergyIntolerance transformer
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
        "fhir_path": "clinicalStatus.text",
        "columns": {"clinical_status_text": {"type": "str"}},
    },
    {
        "fhir_path": "verificationStatus.text",
        "columns": {"verification_status_text": {"type": "str"}},
    },
    {
        "fhir_path": "type",
        "columns": {"type": {"type": "str"}},
    },
    {
        "fhir_path": "criticality",
        "columns": {"criticality": {"type": "str"}},
    },
    {
        "fhir_path": "code.text",
        "columns": {"code_text": {"type": "str"}},
    },
    {
        "fhir_path": "patient",
        "fhir_reference": "patient_reference",
        "columns": {
            "patient_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "patient_display": {"fhir_key": "display", "type": "str"},
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
        "fhir_path": "onsetDateTime",
        "columns": {"onset_date_time": {"type": "datetime"}},
    },
    {
        "fhir_path": "onsetAge",
        "columns": {
            "onset_age_value": {"fhir_key": "value", "type": "str"},
            "onset_age_unit": {"fhir_key": "unit", "type": "str"},
            "onset_age_system": {"fhir_key": "system", "type": "str"},
            "onset_age_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "onsetPeriod",
        "columns": {
            "onset_period_start": {"fhir_key": "start", "type": "datetime"},
            "onset_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "onsetRange",
        "columns": {
            "onset_range_low_value": {"fhir_key": "low.value", "type": "str"},
            "onset_range_low_unit": {"fhir_key": "low.unit", "type": "str"},
            "onset_range_low_system": {"fhir_key": "low.system", "type": "str"},
            "onset_range_low_code": {"fhir_key": "low.code", "type": "str"},
            "onset_range_high_value": {"fhir_key": "high.value", "type": "str"},
            "onset_range_high_unit": {"fhir_key": "high.unit", "type": "str"},
            "onset_range_high_system": {
                "fhir_key": "high.system",
                "type": "str",
            },
            "onset_range_high_code": {"fhir_key": "high.code", "type": "str"},
        },
    },
    {
        "fhir_path": "onsetString",
        "columns": {"onset_string": {"type": "str"}},
    },
    {
        "fhir_path": "recordedDate",
        "columns": {"recorded_date": {"type": "datetime"}},
    },
    {
        "fhir_path": "recorder",
        "fhir_reference": "recorder_reference",
        "columns": {
            "recorder_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "recorder_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "asserter",
        "fhir_reference": "asserter_reference",
        "columns": {
            "asserter_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "asserter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "lastOccurrence",
        "columns": {"last_occurrence": {"type": "datetime"}},
    },
]


class AllergyIntoleranceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'AllergyIntolerance' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the AllergyIntoleranceTransformer instance with the resource
            type 'AllergyIntolerance' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("AllergyIntolerance", None, TRANSFORM_SCHEMA)
