"""
FHIR MedicationDispense transformer
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
        "fhir_path": "statusReasonCodeableConcept.text",
        "columns": {
            "status_reason_codeable_concept_text": {
                "fhir_key": "text",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "statusReasonReference",
        "fhir_reference": "status_reason_reference",
        "columns": {
            "status_reason_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "status_reason_reference_type": {"fhir_key": "type", "type": "str"},
            "status_reason_reference_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "category.text",
        "columns": {"category_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "medicationCodeableConcept.text",
        "columns": {
            "medication_codeable_concept_text": {
                "fhir_key": "text",
                "type": "str",
            }
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
            "medication_reference_type": {"fhir_key": "type", "type": "str"},
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
            "subject_type": {"fhir_key": "type", "type": "str"},
            "subject_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "context",
        "fhir_reference": "context_reference",
        "columns": {
            "context_reference": {"fhir_key": "reference", "type": "str"},
            "context_type": {"fhir_key": "type", "type": "str"},
            "context_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "location",
        "fhir_reference": "location_reference",
        "columns": {
            "location_reference": {"fhir_key": "reference", "type": "str"},
            "location_type": {"fhir_key": "type", "type": "str"},
            "location_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "type.text",
        "columns": {"type_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "quantity",
        "columns": {
            "quantity_value": {"fhir_key": "value", "type": "str"},
            "quantity_unit": {"fhir_key": "unit", "type": "str"},
            "quantity_system": {"fhir_key": "system", "type": "str"},
            "quantity_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "daysSupply",
        "columns": {
            "days_supply_value": {"fhir_key": "value", "type": "str"},
            "days_supply_unit": {"fhir_key": "unit", "type": "str"},
            "days_supply_system": {"fhir_key": "system", "type": "str"},
            "days_supply_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "whenPrepared",
        "columns": {
            "when_prepared": {
                "fhir_key": "whenPrepared",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "whenHandedOver",
        "columns": {
            "when_handed_over": {
                "fhir_key": "whenHandedOver",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "destination",
        "fhir_reference": "destination_reference",
        "columns": {
            "destination_reference": {"fhir_key": "reference", "type": "str"},
            "destination_type": {"fhir_key": "type", "type": "str"},
            "destination_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "receiver",
        "fhir_reference": "receiver_reference",
        "columns": {
            "receiver_reference": {"fhir_key": "reference", "type": "str"},
            "receiver_type": {"fhir_key": "type", "type": "str"},
            "receiver_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "substitution",
        "columns": {
            "substitution_was_substituted": {
                "fhir_key": "wasSubstituted",
                "type": "bool",
            },
            "substitution_type_text": {
                "fhir_key": "type.text",
                "type": "str",
            },
        },
    },
]


class MedicationDispenseTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'MedicationDispense' resource in FHIR.

    Transform MedicationDispense JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the MedicationDispenseTransformer instance with the resource
            type 'MedicationDispense' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("MedicationDispense", None, TRANSFORM_SCHEMA)
