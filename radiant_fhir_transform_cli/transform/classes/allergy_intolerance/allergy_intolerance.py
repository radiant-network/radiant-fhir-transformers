"""FHIR AllergyIntolerance transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "AllergyIntolerance",
    "name": "allergy_intolerance",
    "status": "active",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id", "type": "string"},
                {
                    "name": "resource_type",
                    "path": "resourceType",
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
                {"name": "type", "path": "type", "type": "string"},
                {
                    "name": "criticality",
                    "path": "criticality",
                    "type": "string",
                },
                {"name": "code_text", "path": "code.text", "type": "string"},
                {
                    "name": "patient_reference",
                    "path": "patient.reference",
                    "type": "string",
                },
                {
                    "name": "patient_display",
                    "path": "patient.display",
                    "type": "string",
                },
                {
                    "name": "patient_type",
                    "path": "patient.type",
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
                    "name": "last_occurrence",
                    "path": "lastOccurrence",
                    "type": "dateTime",
                },
            ]
        }
    ],
}


class AllergyIntoleranceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("AllergyIntolerance", None, VIEW_DEFINITION)
