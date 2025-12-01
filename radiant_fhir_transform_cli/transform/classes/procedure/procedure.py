"""FHIR Procedure transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Procedure",
    "name": "procedure",
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
                {"name": "status", "path": "status", "type": "string"},
                {
                    "name": "status_reason_text",
                    "path": "statusReason.text",
                    "type": "string",
                },
                {
                    "name": "category_text",
                    "path": "category.text",
                    "type": "string",
                },
                {"name": "code_text", "path": "code.text", "type": "string"},
                {
                    "name": "subject_reference",
                    "path": "subject.reference",
                    "type": "string",
                },
                {
                    "name": "subject_type",
                    "path": "subject.type",
                    "type": "string",
                },
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {
                    "name": "performed_date_time",
                    "path": "performedDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "performed_period_start",
                    "path": "performedPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "performed_period_end",
                    "path": "performedPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "performed_string",
                    "path": "performedString",
                    "type": "string",
                },
                {
                    "name": "performed_age_value",
                    "path": "performedAge.value",
                    "type": "string",
                },
                {
                    "name": "performed_age_unit",
                    "path": "performedAge.unit",
                    "type": "string",
                },
                {
                    "name": "performed_age_system",
                    "path": "performedAge.system",
                    "type": "string",
                },
                {
                    "name": "performed_age_code",
                    "path": "performedAge.code",
                    "type": "string",
                },
                {
                    "name": "performed_range_low_value",
                    "path": "performedRange.low.value",
                    "type": "string",
                },
                {
                    "name": "performed_range_low_unit",
                    "path": "performedRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "performed_range_low_system",
                    "path": "performedRange.low.system",
                    "type": "string",
                },
                {
                    "name": "performed_range_low_code",
                    "path": "performedRange.low.code",
                    "type": "string",
                },
                {
                    "name": "performed_range_high_value",
                    "path": "performedRange.high.value",
                    "type": "string",
                },
                {
                    "name": "performed_range_high_unit",
                    "path": "performedRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "performed_range_high_system",
                    "path": "performedRange.high.system",
                    "type": "string",
                },
                {
                    "name": "performed_range_high_code",
                    "path": "performedRange.high.code",
                    "type": "string",
                },
                {
                    "name": "recorder_reference",
                    "path": "recorder.reference",
                    "type": "string",
                },
                {
                    "name": "recorder_type",
                    "path": "recorder.type",
                    "type": "string",
                },
                {
                    "name": "recorder_display",
                    "path": "recorder.display",
                    "type": "string",
                },
                {
                    "name": "asserter_reference",
                    "path": "asserter.reference",
                    "type": "string",
                },
                {
                    "name": "asserter_type",
                    "path": "asserter.type",
                    "type": "string",
                },
                {
                    "name": "asserter_display",
                    "path": "asserter.display",
                    "type": "string",
                },
                {
                    "name": "location_reference",
                    "path": "location.reference",
                    "type": "string",
                },
                {
                    "name": "location_type",
                    "path": "location.type",
                    "type": "string",
                },
                {
                    "name": "location_display",
                    "path": "location.display",
                    "type": "string",
                },
                {
                    "name": "outcome_text",
                    "path": "outcome.text",
                    "type": "string",
                },
            ]
        }
    ],
}


class ProcedureTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Procedure", None, VIEW_DEFINITION)
