"""FHIR MedicationRequest transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationRequest",
    "name": "medication_request",
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
                {"name": "intent", "path": "intent", "type": "string"},
                {"name": "priority", "path": "priority", "type": "string"},
                {
                    "name": "do_not_perform",
                    "path": "doNotPerform",
                    "type": "string",
                },
                {
                    "name": "reported_boolean",
                    "path": "reportedBoolean",
                    "type": "string",
                },
                {
                    "name": "reported_reference_reference",
                    "path": "reportedReference.reference",
                    "type": "string",
                },
                {
                    "name": "reported_reference_type",
                    "path": "reportedReference.type",
                    "type": "string",
                },
                {
                    "name": "reported_reference_display",
                    "path": "reportedReference.display",
                    "type": "string",
                },
                {
                    "name": "medication_codeable_concept_text",
                    "path": "medicationCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "medication_reference_reference",
                    "path": "medicationReference.reference",
                    "type": "string",
                },
                {
                    "name": "medication_reference_type",
                    "path": "medicationReference.type",
                    "type": "string",
                },
                {
                    "name": "medication_reference_display",
                    "path": "medicationReference.display",
                    "type": "string",
                },
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
                    "name": "authored_on",
                    "path": "authoredOn",
                    "type": "dateTime",
                },
                {
                    "name": "requester_reference",
                    "path": "requester.reference",
                    "type": "string",
                },
                {
                    "name": "requester_type",
                    "path": "requester.type",
                    "type": "string",
                },
                {
                    "name": "requester_display",
                    "path": "requester.display",
                    "type": "string",
                },
                {
                    "name": "performer_reference",
                    "path": "performer.reference",
                    "type": "string",
                },
                {
                    "name": "performer_type",
                    "path": "performer.type",
                    "type": "string",
                },
                {
                    "name": "performer_display",
                    "path": "performer.display",
                    "type": "string",
                },
                {
                    "name": "performer_type_text",
                    "path": "performerType.text",
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
                    "name": "group_identifier_use",
                    "path": "groupIdentifier.use",
                    "type": "string",
                },
                {
                    "name": "group_identifier_system",
                    "path": "groupIdentifier.system",
                    "type": "string",
                },
                {
                    "name": "group_identifier_value",
                    "path": "groupIdentifier.value",
                    "type": "string",
                },
                {
                    "name": "course_of_therapy_type_text",
                    "path": "courseOfTherapyType.text",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_quantity_value",
                    "path": "dispenseRequest.initialFill.quantity.value",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_quantity_unit",
                    "path": "dispenseRequest.initialFill.quantity.unit",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_quantity_system",
                    "path": "dispenseRequest.initialFill.quantity.system",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_quantity_code",
                    "path": "dispenseRequest.initialFill.quantity.code",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_duration_value",
                    "path": "dispenseRequest.initialFill.duration.value",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_duration_unit",
                    "path": "dispenseRequest.initialFill.duration.unit",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_duration_system",
                    "path": "dispenseRequest.initialFill.duration.system",
                    "type": "string",
                },
                {
                    "name": "dispense_request_initial_fill_duration_code",
                    "path": "dispenseRequest.initialFill.duration.code",
                    "type": "string",
                },
                {
                    "name": "dispense_request_dispense_interval_value",
                    "path": "dispenseRequest.dispenseInterval.value",
                    "type": "string",
                },
                {
                    "name": "dispense_request_dispense_interval_unit",
                    "path": "dispenseRequest.dispenseInterval.unit",
                    "type": "string",
                },
                {
                    "name": "dispense_request_dispense_interval_system",
                    "path": "dispenseRequest.dispenseInterval.system",
                    "type": "string",
                },
                {
                    "name": "dispense_request_dispense_interval_code",
                    "path": "dispenseRequest.dispenseInterval.code",
                    "type": "string",
                },
                {
                    "name": "dispense_request_validity_period_start",
                    "path": "dispenseRequest.validityPeriod.start",
                    "type": "dateTime",
                },
                {
                    "name": "dispense_request_validity_period_end",
                    "path": "dispenseRequest.validityPeriod.end",
                    "type": "dateTime",
                },
                {
                    "name": "dispense_request_number_of_repeats_allowed",
                    "path": "dispenseRequest.numberOfRepeatsAllowed",
                    "type": "integer",
                },
                {
                    "name": "dispense_request_quantity_value",
                    "path": "dispenseRequest.quantity.value",
                    "type": "string",
                },
                {
                    "name": "dispense_request_quantity_unit",
                    "path": "dispenseRequest.quantity.unit",
                    "type": "string",
                },
                {
                    "name": "dispense_request_quantity_system",
                    "path": "dispenseRequest.quantity.system",
                    "type": "string",
                },
                {
                    "name": "dispense_request_quantity_code",
                    "path": "dispenseRequest.quantity.code",
                    "type": "string",
                },
                {
                    "name": "dispense_request_expected_supply_duration_value",
                    "path": "dispenseRequest.expectedSupplyDuration.value",
                    "type": "string",
                },
                {
                    "name": "dispense_request_expected_supply_duration_unit",
                    "path": "dispenseRequest.expectedSupplyDuration.unit",
                    "type": "string",
                },
                {
                    "name": "dispense_request_expected_supply_duration_system",
                    "path": "dispenseRequest.expectedSupplyDuration.system",
                    "type": "string",
                },
                {
                    "name": "dispense_request_expected_supply_duration_code",
                    "path": "dispenseRequest.expectedSupplyDuration.code",
                    "type": "string",
                },
                {
                    "name": "dispense_request_performer_reference",
                    "path": "dispenseRequest.performer.reference",
                    "type": "string",
                },
                {
                    "name": "dispense_request_performer_type",
                    "path": "dispenseRequest.performer.type",
                    "type": "string",
                },
                {
                    "name": "dispense_request_performer_display",
                    "path": "dispenseRequest.performer.display",
                    "type": "string",
                },
                {
                    "name": "substitution_allowed_boolean",
                    "path": "substitution.allowedBoolean",
                    "type": "string",
                },
                {
                    "name": "substitution_allowed_codeable_concept_text",
                    "path": "substitution.allowedCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "substitution_reason_text",
                    "path": "substitution.reason.text",
                    "type": "string",
                },
                {
                    "name": "prior_prescription_reference",
                    "path": "priorPrescription.reference",
                    "type": "string",
                },
                {
                    "name": "prior_prescription_type",
                    "path": "priorPrescription.type",
                    "type": "string",
                },
                {
                    "name": "prior_prescription_display",
                    "path": "priorPrescription.display",
                    "type": "string",
                },
            ]
        }
    ],
}


class MedicationRequestTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationRequest", None, VIEW_DEFINITION)
