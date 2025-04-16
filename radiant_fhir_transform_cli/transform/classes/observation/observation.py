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
        "fhir_path": "valueQuantity.value",
        "columns": {
            "value_quantity_value": "valueQuantity.value",
        },
    },
]

TRANSFORM_DICT_OLD = {
    "id": "id",
    "resource_type": "resourceType",
    "status": "status",
    "code_text": "code.text",
    # "subject_reference": "subject.reference",
    # "notes": "note.text",
    # "value_quantity_value": "valueQuantity.value",
    # "value_quantity_unit": "valueQuantity.unit",
    # "value_quantity_code": "valueQuantity.code",
    # "value_quantity_system": "valueQuantity.system",
    # "value_codeable_concept_coding_codes": "valueCodeableConcept.coding.code",
    # "value_codeable_concept_coding_displays": "valueCodeableConcept.coding.display",
    # "value_codeable_concept_coding_systems": "valueCodeableConcept.coding.system",
    # "value_codeable_concept_text": "valueCodeableConcept.text",
    # "value_range_low_value": "valueRange.low.value",
    # "value_range_low_unit": "valueRange.low.unit",
    # "value_range_high_value": "valueRange.high.value",
    # "value_range_high_unit": "valueRange.high.unit",
    # "value_ratio_numerator_value": "valueRation.numerator.value",
    # "value_ratio_numerator_unit": "valueRation.numerator.unit",
    # "value_ratio_numerator_code": "valueRation.numerator.code",
    # "value_ratio_numerator_system": "valueRation.numerator.system",
    # "value_ratio_denominator_value": "valueRation.denominator.value",
    # "value_ratio_denominator_unit": "valueRation.denominator.unit",
    # "value_ratio_denominator_code": "valueRation.denominator.code",
    # "value_ratio_denominator_system": "valueRation.denominator.system",
    # "value_string": "valueString",
    # # "component_code_coding_codes": "component.code.coding.code",
    # # "component_code_coding_systems": "component.code.coding.system",
    # # "component_code_coding_display": "component.code.coding.display",
    # "component_coding_texts": "component.code.text",
    # "component_value_quantity_values": "component.valueQuantity.value",
    # "component_value_quantity_units": "component.valueQuantity.unit",
    # "component_value_quantity_codes": "component.valueQuantity.code",
    # "component_value_quantity_system": "component.valueQuantity.system",
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
