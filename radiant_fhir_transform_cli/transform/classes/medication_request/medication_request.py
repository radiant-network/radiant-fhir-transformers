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
            "resource_type": {"fhir_key": "resourceType", "type": "str"}
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "intent",
        "columns": {"intent": {"fhir_key": "intent", "type": "str"}},
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
            "reported_reference_type": {
                "fhir_key": "type",
                "type": "str",
            },
            "reported_reference_identifier_use": {
                "fhir_key": "identifier.use",
                "type": "str",
            },
            "reported_reference_identifier_system": {
                "fhir_key": "identifier.system",
                "type": "str",
            },
            "reported_reference_identifier_value": {
                "fhir_key": "identifier.value",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "reportedBoolean",
        "columns": {
            "reported_boolean": {"fhir_key": "reported_boolean", "type": "bool"}
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
            "medication_reference_type": {
                "fhir_key": "type",
                "type": "str",
            },
            "medication_reference_identifier_use": {
                "fhir_key": "identifier.use",
                "type": "str",
            },
            "medication_reference_identifier_system": {
                "fhir_key": "identifier.system",
                "type": "str",
            },
            "medication_reference_identifier_value": {
                "fhir_key": "identifier.value",
                "type": "str",
            },
        },
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
            "subject_type": {
                "fhir_key": "type",
                "type": "str",
            },
            "subject_identifier_use": {
                "fhir_key": "identifier.use",
                "type": "str",
            },
            "subject_identifier_system": {
                "fhir_key": "identifier.system",
                "type": "str",
            },
            "subject_identifier_value": {
                "fhir_key": "identifier.value",
                "type": "str",
            },
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
            "encounter_type": {
                "fhir_key": "type",
                "type": "str",
            },
            "encounter_identifier_use": {
                "fhir_key": "identifier.use",
                "type": "str",
            },
            "encounter_identifier_system": {
                "fhir_key": "identifier.system",
                "type": "str",
            },
            "encounter_identifier_value": {
                "fhir_key": "identifier.value",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "authoredOn",
        "columns": {
            "authored_on": {"fhir_key": "authoredOn", "type": "date"},
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
        "fhir_path": "medicationCodeableConcept.text",
        "columns": {
            "medication_codeable_concept_text": {
                "fhir_key": "medicationCodeableConcept.text",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "dispenseRequest",
        "columns": {
            "dispense_request_number_of_repeats_allowed": {
                "fhir_key": "numberOfRepeatsAllowed",
                "type": "int",
            },
            "dispense_request_quantity_value": {
                "fhir_key": "quantity.value",
                "type": "int",
            },
            "dispense_request_quantity_unit": {
                "fhir_key": "quantity.unit",
                "type": "str",
            },
            "dispense_request_quantity_code": {
                "fhir_key": "quantity.code",
                "type": "str",
            },
            "dispense_request_quantity_system": {
                "fhir_key": "quantity.system",
                "type": "str",
            },
        },
    },
]


class MedicationRequestTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Medication' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ObservationTransformer instance with the resource
            type 'Observation' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("MedicationRequest", None, TRANSFORM_SCHEMA)
