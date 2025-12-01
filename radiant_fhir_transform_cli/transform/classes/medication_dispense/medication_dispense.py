"""FHIR MedicationDispense transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense",
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
                    "name": "status_reason_codeable_concept_text",
                    "path": "statusReasonCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "status_reason_reference",
                    "path": "statusReasonReference.reference",
                    "type": "string",
                },
                {
                    "name": "status_reason_reference_type",
                    "path": "statusReasonReference.type",
                    "type": "string",
                },
                {
                    "name": "status_reason_reference_display",
                    "path": "statusReasonReference.display",
                    "type": "string",
                },
                {"name": "category_text", "path": "category.text", "type": "string"},
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
                {"name": "subject_type", "path": "subject.type", "type": "string"},
                {
                    "name": "subject_display",
                    "path": "subject.display",
                    "type": "string",
                },
                {
                    "name": "context_reference",
                    "path": "context.reference",
                    "type": "string",
                },
                {"name": "context_type", "path": "context.type", "type": "string"},
                {
                    "name": "context_display",
                    "path": "context.display",
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
                {"name": "type_text", "path": "type.text", "type": "string"},
                {
                    "name": "quantity_value",
                    "path": "quantity.value",
                    "type": "string",
                },
                {
                    "name": "quantity_unit",
                    "path": "quantity.unit",
                    "type": "string",
                },
                {
                    "name": "quantity_system",
                    "path": "quantity.system",
                    "type": "string",
                },
                {
                    "name": "quantity_code",
                    "path": "quantity.code",
                    "type": "string",
                },
                {
                    "name": "days_supply_value",
                    "path": "daysSupply.value",
                    "type": "string",
                },
                {
                    "name": "days_supply_unit",
                    "path": "daysSupply.unit",
                    "type": "string",
                },
                {
                    "name": "days_supply_system",
                    "path": "daysSupply.system",
                    "type": "string",
                },
                {
                    "name": "days_supply_code",
                    "path": "daysSupply.code",
                    "type": "string",
                },
                {
                    "name": "when_prepared",
                    "path": "whenPrepared",
                    "type": "dateTime",
                },
                {
                    "name": "when_handed_over",
                    "path": "whenHandedOver",
                    "type": "dateTime",
                },
                {
                    "name": "destination_reference",
                    "path": "destination.reference",
                    "type": "string",
                },
                {
                    "name": "destination_type",
                    "path": "destination.type",
                    "type": "string",
                },
                {
                    "name": "destination_display",
                    "path": "destination.display",
                    "type": "string",
                },
                {
                    "name": "substitution_was_substituted",
                    "path": "substitution.wasSubstituted",
                    "type": "boolean",
                },
                {
                    "name": "substitution_type_text",
                    "path": "substitution.type.text",
                    "type": "string",
                },
            ]
        }
    ],
}


class MedicationDispenseTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", None, VIEW_DEFINITION)
