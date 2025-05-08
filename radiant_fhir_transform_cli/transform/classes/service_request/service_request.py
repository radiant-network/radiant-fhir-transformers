"""
FHIR ServiceRequest transformer
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
        "columns": {
            "resource_type": {"type": "str"}
        },
    },
    {
        "fhir_path": "text.status",
        "columns": {
            "text_status": {"type": "str"}
        },
    },
    
    {
        "fhir_path": "status",
        "columns": {
            "status": { "type": "str"}
        },
    },
    {
        "fhir_path": "intent",
        "columns": {
            "intent": {"type": "str"}
        },
    },
    {
        "fhir_path": "priority",
        "columns": {
            "priority": { "type": "str"}
        },
    },  
    {
        "fhir_path": "doNotPerform",
        "columns": {
            "do_not_perform": { "type": "str"}
        },
    },  
    {
        "fhir_path": "code.text",
        "columns": {
            "code_text": { "type": "str"},
        },
    },
    {
        "fhir_path": "quantityQuantity",
        "columns": {
            "quantity_quantity": { "type": "str"},
        },
    },
    {
        "fhir_path": "quantityRatio",
        "columns": {
            "quantity_ratio": { "type": "str"},
        },
    },
    {
        "fhir_path": "quantityRange",
        "columns": {
            "quantity_range": { "type": "str"},
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
        "fhir_path": "occurrenceDateTime",
        "columns": {
            "occurence_date_time": {"type": "str"}
        },
    },
    {
        "fhir_path": "occurrencePeriod",
        "columns": {
            "occurence_period_start": {"fhir_key": "start","type": "str"},
            "occurence_period_end": {"fhir_key": "end","type": "str"},
        },
    },
    {
        "fhir_path": "occurrenceTiming.repeat",
        "columns": {
            "occurence_timing_repeat_count": {"fhir_key": "count", "type": "str"},
            "occurence_timing_repeat_count_max": {"fhir_key": "countMax", "type": "str"},
            "occurence_timing_repeat_frequency": {"fhir_key": "frequency", "type": "str"},
            "occurence_timing_repeat_period": {"fhir_key": "period", "type": "str"},
            "occurence_timing_repeat_period_unit": {"fhir_key": "periodUnit", "type": "str"},
        },
    },
    {
        "fhir_path": "asNeededBoolean.value",
        "columns": {
            "as_needed_boolean_value": {"type": "str"}
        },
    },
    {
        "fhir_path": "asNeededCodeableConcept.text",
        "columns": {
            "as_needed_codeable_concept_text": {"type": "str"}
        },
    },
    {
        "fhir_path": "authoredOn",
        "columns": {
            "authored_on": {"type": "str"}
        },
    },
    {
        "fhir_path": "requester",
        "fhir_reference": "requester_reference",
        "columns": {
            "requester_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "requester_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "performerType",
        "columns": {
            "performer_type_coding": {"fhir_key": "coding", "type": "str"},
            "performer_type_text": {"fhir_key": "text", "type": "str"}
        },
    },
    {
        "fhir_path": "patientInstruction",
        "columns": {
            "patient_instruction": { "type": "str"},
        },
    },
]


class ServiceRequestTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'ServiceRequest' resource in FHIR.

    Transform ServiceRequest JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ServiceRequestTransformer instance with the resource
            type 'ServiceRequest' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("ServiceRequest", None, TRANSFORM_SCHEMA)