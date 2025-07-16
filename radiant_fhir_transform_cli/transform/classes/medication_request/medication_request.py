"""
FHIR MedicationRequest transformer
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
            "resource_type": {
                "fhir_key": "resourceType",
                "type": "str",
            }
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
        "fhir_path": "intent",
        "columns": {"intent": {"fhir_key": "intent", "type": "str"}},
    },
    {
        "fhir_path": "priority",
        "columns": {"priority": {"fhir_key": "priority", "type": "str"}},
    },
    {
        "fhir_path": "doNotPerform",
        "columns": {
            "do_not_perform": {"fhir_key": "doNotPerform", "type": "bool"}
        },
    },
    {
        "fhir_path": "reportedBoolean",
        "columns": {
            "reported_boolean": {"fhir_key": "reportedBoolean", "type": "bool"}
        },
    },
    {
        "fhir_path": "reportedReference",
        "fhir_reference": "reported_reference_reference",
        "columns": {
            "reported_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "reported_reference_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "medicationCodeableConcept.text",
        "columns": {
            "medication_codeable_concept_text": {
                "fhir_key": "text",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "medicationReference",
        "fhir_reference": "medication_reference_reference",
        "columns": {
            "medication_reference_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "medication_reference_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
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
        "fhir_path": "authoredOn",
        "columns": {
            "authored_on": {"fhir_key": "authoredOn", "type": "datetime"},
        },
    },
    {
        "fhir_path": "requester",
        "fhir_reference": "requester_reference",
        "columns": {
            "requester_reference": {"fhir_key": "reference", "type": "str"},
            "requester_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "performer",
        "fhir_reference": "performer_reference",
        "columns": {
            "performer_reference": {"fhir_key": "reference", "type": "str"},
            "performer_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "performerType.text",
        "columns": {
            "performer_type_text": {"fhir_key": "text", "type": "str"},
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
        "fhir_path": "groupIdentifier",
        "columns": {
            "group_identifier_use": {"fhir_key": "use", "type": "str"},
            "group_identifier_system": {"fhir_key": "system", "type": "str"},
            "group_identifier_value": {"fhir_key": "value", "type": "str"},
        },
    },
    {
        "fhir_path": "courseOfTherapyType.text",
        "columns": {
            "course_of_therapy_type_text": {"fhir_key": "text", "type": "str"}
        },
    },
    {
        "fhir_path": "dispenseRequest",
        "fhir_reference": "dispense_request_performer_reference",
        "columns": {
            "dispense_request_initial_fill_quantity_value": {
                "fhir_key": "initialFill.quantity.value",
                "type": "str",
            },
            "dispense_request_initial_fill_quantity_unit": {
                "fhir_key": "initialFill.quantity.unit",
                "type": "str",
            },
            "dispense_request_initial_fill_quantity_system": {
                "fhir_key": "initialFill.quantity.system",
                "type": "str",
            },
            "dispense_request_initial_fill_quantity_code": {
                "fhir_key": "initialFill.quantity.code",
                "type": "str",
            },
            "dispense_request_initial_fill_duration_value": {
                "fhir_key": "initialFill.duration.value",
                "type": "str",
            },
            "dispense_request_initial_fill_duration_unit": {
                "fhir_key": "initialFill.duration.unit",
                "type": "str",
            },
            "dispense_request_initial_fill_duration_system": {
                "fhir_key": "initialFill.duration.system",
                "type": "str",
            },
            "dispense_request_initial_fill_duration_code": {
                "fhir_key": "initialFill.duration.code",
                "type": "str",
            },
            "dispense_request_dispense_interval_value": {
                "fhir_key": "dispenseInterval.value",
                "type": "str",
            },
            "dispense_request_dispense_interval_unit": {
                "fhir_key": "dispenseInterval.unit",
                "type": "str",
            },
            "dispense_request_dispense_interval_system": {
                "fhir_key": "dispenseInterval.system",
                "type": "str",
            },
            "dispense_request_dispense_interval_code": {
                "fhir_key": "dispenseInterval.code",
                "type": "str",
            },
            "dispense_request_validity_period_start": {
                "fhir_key": "validityPeriod.start",
                "type": "datetime",
            },
            "dispense_request_validity_period_end": {
                "fhir_key": "validityPeriod.end",
                "type": "datetime",
            },
            "dispense_request_number_of_repeats_allowed": {
                "fhir_key": "numberOfRepeatsAllowed",
                "type": "int",
            },
            "dispense_request_quantity_value": {
                "fhir_key": "quantity.value",
                "type": "str",
            },
            "dispense_request_quantity_unit": {
                "fhir_key": "quantity.unit",
                "type": "str",
            },
            "dispense_request_quantity_system": {
                "fhir_key": "quantity.system",
                "type": "str",
            },
            "dispense_request_quantity_code": {
                "fhir_key": "quantity.code",
                "type": "str",
            },
            "dispense_request_expected_supply_duration_value": {
                "fhir_key": "expectedSupplyDuration.value",
                "type": "str",
            },
            "dispense_request_expected_supply_duration_unit": {
                "fhir_key": "expectedSupplyDuration.unit",
                "type": "str",
            },
            "dispense_request_expected_supply_duration_system": {
                "fhir_key": "expectedSupplyDuration.system",
                "type": "str",
            },
            "dispense_request_expected_supply_duration_code": {
                "fhir_key": "expectedSupplyDuration.code",
                "type": "str",
            },
            "dispense_request_performer_reference": {
                "fhir_key": "performer.reference",
                "type": "str",
            },
            "dispense_request_performer_display": {
                "fhir_key": "performer.display",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "substitution",
        "columns": {
            "substitution_allowed_boolean": {
                "fhir_key": "allowedBoolean",
                "type": "bool",
            },
            "substitution_allowed_codeable_concept_text": {
                "fhir_key": "allowedCodeableConcept.text",
                "type": "str",
            },
            "substitution_reason_text": {
                "fhir_key": "reason.text",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "priorPrescription",
        "fhir_reference": "prior_prescription_reference",
        "columns": {
            "prior_prescription_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "prior_prescription_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class MedicationRequestTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationRequest' resource in FHIR.

    Transform MedicationRequest JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the MedicationRequestTransformer instance with the resource
            type 'MedicationRequest' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("MedicationRequest", None, TRANSFORM_SCHEMA)
