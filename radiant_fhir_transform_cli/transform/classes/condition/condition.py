"""FHIR Condition transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "code_text",
                    "path": "code.text",
                    "type": "string",
                },
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "onset_date_time",
                    "path": "onsetDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "onset_age_value",
                    "path": "onsetAge.value",
                    "type": "string",
                },
                {
                    "name": "onset_age_unit",
                    "path": "onsetAge.unit",
                    "type": "string",
                },
                {
                    "name": "onset_age_system",
                    "path": "onsetAge.system",
                    "type": "string",
                },
                {
                    "name": "onset_age_code",
                    "path": "onsetAge.code",
                    "type": "string",
                },
                {
                    "name": "onset_period_start",
                    "path": "onsetPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "onset_period_end",
                    "path": "onsetPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "onset_range_low_value",
                    "path": "onsetRange.low.value",
                    "type": "string",
                },
                {
                    "name": "onset_range_low_unit",
                    "path": "onsetRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "onset_range_low_system",
                    "path": "onsetRange.low.system",
                    "type": "string",
                },
                {
                    "name": "onset_range_low_code",
                    "path": "onsetRange.low.code",
                    "type": "string",
                },
                {
                    "name": "onset_range_high_value",
                    "path": "onsetRange.high.value",
                    "type": "string",
                },
                {
                    "name": "onset_range_high_unit",
                    "path": "onsetRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "onset_range_high_system",
                    "path": "onsetRange.high.system",
                    "type": "string",
                },
                {
                    "name": "onset_range_high_code",
                    "path": "onsetRange.high.code",
                    "type": "string",
                },
                {
                    "name": "onset_string",
                    "path": "onsetString",
                    "type": "string",
                },
                {
                    "name": "abatement_date_time",
                    "path": "abatementDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "abatement_age_value",
                    "path": "abatementAge.value",
                    "type": "string",
                },
                {
                    "name": "abatement_age_unit",
                    "path": "abatementAge.unit",
                    "type": "string",
                },
                {
                    "name": "abatement_age_system",
                    "path": "abatementAge.system",
                    "type": "string",
                },
                {
                    "name": "abatement_age_code",
                    "path": "abatementAge.code",
                    "type": "string",
                },
                {
                    "name": "abatement_period_start",
                    "path": "abatementPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "abatement_period_end",
                    "path": "abatementPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "abatement_range_low_value",
                    "path": "abatementRange.low.value",
                    "type": "string",
                },
                {
                    "name": "abatement_range_low_unit",
                    "path": "abatementRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "abatement_range_low_system",
                    "path": "abatementRange.low.system",
                    "type": "string",
                },
                {
                    "name": "abatement_range_low_code",
                    "path": "abatementRange.low.code",
                    "type": "string",
                },
                {
                    "name": "abatement_range_high_value",
                    "path": "abatementRange.high.value",
                    "type": "string",
                },
                {
                    "name": "abatement_range_high_unit",
                    "path": "abatementRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "abatement_range_high_system",
                    "path": "abatementRange.high.system",
                    "type": "string",
                },
                {
                    "name": "abatement_range_high_code",
                    "path": "abatementRange.high.code",
                    "type": "string",
                },
                {
                    "name": "abatement_string",
                    "path": "abatementString",
                    "type": "string",
                },
                {
                    "name": "recorded_date",
                    "path": "recordedDate",
                    "type": "dateTime",
                },
                {
                    "name": "recorder_reference",
                    "path": "recorder.reference",
                    "type": "string",
                },
                {
                    "name": "recorder_display",
                    "path": "recorder.display",
                    "type": "string",
                },
                {
                    "name": "recorder_type",
                    "path": "recorder.type",
                    "type": "string",
                },
                {
                    "name": "asserter_reference",
                    "path": "asserter.reference",
                    "type": "string",
                },
                {
                    "name": "asserter_display",
                    "path": "asserter.display",
                    "type": "string",
                },
                {
                    "name": "asserter_type",
                    "path": "asserter.type",
                    "type": "string",
                },
                {
                    "name": "clinical_status_text",
                    "path": "clinicalStatus.text",
                    "type": "string",
                },
                {
                    "name": "verification_status_text",
                    "path": "verificationStatus.text",
                    "type": "string",
                },
                {
                    "name": "severity_text",
                    "path": "severity.text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConditionTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Condition", None, VIEW_DEFINITION)
