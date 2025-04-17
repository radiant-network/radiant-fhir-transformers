"""
FHIR Observation transformer

Map nested fields in the Observation resource to keys in a flat dict which
represents a row in a csv file

Transform Dictionary
--------------------
- Keys are output columns in a csv file.

- Values are FHIR path expressions to
  the field value to be extracted from the FHIR JSON object
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

OBSERVATION_CATEGORY = (
    "http://terminology.hl7.org/CodeSystem/observation-category"
)


TRANSFORM_DICT = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": "id",
        },
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": "resourceType",
        },
    },
    {
        "fhir_path": "status",
        "columns": {
            "status": "status",
        },
    },
    {
        "fhir_path": "code.text",
        "columns": {
            "code_coding_text": "text",
        },
    },
    {
        "fhir_path": "subject",
        "columns": {
            "subject_reference": "reference",
            "subject_display": "display",
        },
    },
    {
        "fhir_path": "encounter.reference",
        "columns": {
            "encounter_reference": "encounter.reference",
        },
    },
    {
        "fhir_path": "encounter.identifier",
        "columns": {
            "encounter_identifier_use": "use",
            "encounter_identifier_system": "system",
            "encounter_identifier_value": "value",
        },
    },
    {
        "fhir_path": "encounter.display",
        "columns": {
            "encounter_display": "encounter.display",
        },
    },
    {
        "fhir_path": "valueQuantity",
        "columns": {
            "value_quantity_value": "value",
            "value_quantity_unit": "unit",
            "value_quantity_code": "code",
            "value_quantity_system": "system",
        },
    },
    {
        "fhir_path": "valueCodeableConcept.text",
        "columns": {
            "value_codeable_concept_text": "valueCodeableConcept.text",
        },
    },
    {
        "fhir_path": "valueRange.low",
        "columns": {
            "value_range_low_value": "value",
            "value_range_low_unit": "unit",
        },
    },
    {
        "fhir_path": "valueRange.high",
        "columns": {
            "value_range_high_value": "value",
            "value_range_high_unit": "unit",
        },
    },
    {
        "fhir_path": "valueRatio.numerator",
        "columns": {
            "value_ratio_numerator_value": "value",
            "value_ratio_numerator_unit": "unit",
            "value_ratio_numerator_code": "code",
        },
    },
    {
        "fhir_path": "valueRatio.denominator",
        "columns": {
            "value_ratio_denominator_value": "value",
            "value_ratio_denominator_unit": "unit",
            "value_ratio_denominator_code": "code",
        },
    },
    {
        "fhir_path": "valueString",
        "columns": {
            "value_string": "valueString",
        },
    },
    {
        "fhir_path": "valueBoolean",
        "columns": {
            "value_boolean": "valueBoolean",
        },
    },
    {
        "fhir_path": "valueInteger",
        "columns": {
            "value_integer": "valueInteger",
        },
    },
    {
        "fhir_path": "effectiveDateTime",
        "columns": {
            "effective_datetime": "effectiveDateTime",
        },
    },
    {
        "fhir_path": "issued",
        "columns": {
            "issued": "issued",
        },
    },
    {
        "fhir_path": "effectivePeriod",
        "columns": {
            "effective_period_start": "start",
            "effective_period_end": "end",
        },
    },
]

TRANSFORM_DICT_OLD = {
    # "notes": "note.text",
    # "value_codeable_concept_coding_codes": "valueCodeableConcept.coding.code",
    # "value_codeable_concept_coding_displays": "valueCodeableConcept.coding.display",
    # "value_codeable_concept_coding_systems": "valueCodeableConcept.coding.system",
    # "value_codeable_concept_text": "valueCodeableConcept.text",
    # # "component_code_coding_codes": "component.code.coding.code",
    # # "component_code_coding_systems": "component.code.coding.system",
    # # "component_code_coding_display": "component.code.coding.display",
}


class ObservationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Observation' resource in FHIR.

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
        super().__init__("Observation", None, TRANSFORM_DICT)
