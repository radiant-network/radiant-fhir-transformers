"""
FHIR Condition transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


TRANSFORM_SCHEMA = [
    {
        "fhir_path": "id",
        "columns": {"id": {"type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {"resource_type": {"type": "str"}},
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": {"type": "str"},
        },
    },
    # subject
    {
        "fhir_path": "subject",
        "fhir_reference": "subject_reference",
        "columns": {
            "subject_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "subject_display": {"fhir_key": "display", "type": "str"},
            "subject_type": {"fhir_key": "type", "type": "str"},
        },
    },
    # encounter
    {
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "encounter_display": {"fhir_key": "display", "type": "str"},
            "encounter_type": {"fhir_key": "type", "type": "str"},
        },
    },
    # onset
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
    # abatement
    {
        "fhir_path": "abatementDateTime",
        "columns": {"abatement_date_time": {"type": "datetime"}},
    },
    {
        "fhir_path": "abatementAge",
        "columns": {
            "abatement_age_value": {"fhir_key": "value", "type": "str"},
            "abatement_age_unit": {"fhir_key": "unit", "type": "str"},
            "abatement_age_system": {"fhir_key": "system", "type": "str"},
            "abatement_age_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "abatementPeriod",
        "columns": {
            "abatement_period_start": {"fhir_key": "start", "type": "datetime"},
            "abatement_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
    {
        "fhir_path": "abatementRange",
        "columns": {
            "abatement_range_low_value": {
                "fhir_key": "low.value",
                "type": "str",
            },
            "abatement_range_low_unit": {"fhir_key": "low.unit", "type": "str"},
            "abatement_range_low_system": {
                "fhir_key": "low.system",
                "type": "str",
            },
            "abatement_range_low_code": {"fhir_key": "low.code", "type": "str"},
            "abatement_range_high_value": {
                "fhir_key": "high.value",
                "type": "str",
            },
            "abatement_range_high_unit": {
                "fhir_key": "high.unit",
                "type": "str",
            },
            "abatement_range_high_system": {
                "fhir_key": "high.system",
                "type": "str",
            },
            "abatement_range_high_code": {
                "fhir_key": "high.code",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "abatementString",
        "columns": {"abatement_string": {"type": "str"}},
    },
    # recorded Date
    {
        "fhir_path": "recordedDate",
        "columns": {"recorded_date": {"type": "datetime"}},
    },
    # recorder
    {
        "fhir_path": "recorder",
        "fhir_reference": "recorder_reference",
        "columns": {
            "recorder_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "recorder_display": {"fhir_key": "display", "type": "str"},
            "recorder_type": {"fhir_key": "type", "type": "str"},
        },
    },
    # asserter
    {
        "fhir_path": "asserter",
        "fhir_reference": "asserter_reference",
        "columns": {
            "asserter_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "asserter_display": {"fhir_key": "display", "type": "str"},
            "asserter_type": {"fhir_key": "type", "type": "str"},
        },
    },
    {
        "fhir_path": "clinicalStatus.text",
        "columns": {
            "clinical_status_text": {"type": "str"},
        },
    },
    {
        "fhir_path": "verificationStatus.text",
        "columns": {
            "verification_status_text": {"type": "str"},
        },
    },
    {
        "fhir_path": "severity.text",
        "columns": {
            "severity_text": {"type": "str"},
        },
    },
]


class ConditionTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Condition' resource in FHIR.

    Transform Condition JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ConditionTransformer instance with the resource
            type 'Condition' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Condition", None, TRANSFORM_SCHEMA)
