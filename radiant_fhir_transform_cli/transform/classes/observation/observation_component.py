"""
FHIR Observation Component transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "component",
        "columns": {
            "component_data_absent_reason_system": {
                "fhir_key": "dataAbsentReason.system",
                "type": "str",
            },
            "component_data_absent_reason_code": {
                "fhir_key": "dataAbsentReason.code",
                "type": "str",
            },
            "component_data_absent_reason_display": {
                "fhir_key": "dataAbsentReason.display",
                "type": "str",
            },
            "component_code_text": {
                "fhir_key": "code.text",
                "type": "str",
            },
            "component_value_quantity_value": {
                "fhir_key": "valueQuantity.value",
                "type": "str",
            },
            "component_value_quantity_unit": {
                "fhir_key": "valueQuantity.unit",
                "type": "str",
            },
            "component_value_quantity_code": {
                "fhir_key": "valueQuantity.code",
                "type": "str",
            },
            "component_value_quantity_system": {
                "fhir_key": "valueQuantity.system",
                "type": "str",
            },
            "component_value_range_low_value": {
                "fhir_key": "valueRange.low.value",
                "type": "int",
            },
            "component_value_range_low_unit": {
                "fhir_key": "valueRange.low.unit",
                "type": "str",
            },
            "component_value_range_high_value": {
                "fhir_key": "valueRange.high.value",
                "type": "int",
            },
            "component_value_range_high_unit": {
                "fhir_key": "valueRange.high.unit",
                "type": "str",
            },
            "component_value_ratio_numerator_value": {
                "fhir_key": "valueRatio.numerator.value",
                "type": "int",
            },
            "component_value_ratio_numerator_unit": {
                "fhir_key": "valueRatio.numerator.unit",
                "type": "str",
            },
            "component_value_ratio_numerator_code": {
                "fhir_key": "valueRatio.numerator.code",
                "type": "str",
            },
            "component_value_ratio_denominator_value": {
                "fhir_key": "valueRatio.denominator.value",
                "type": "int",
            },
            "component_value_ratio_denominator_unit": {
                "fhir_key": "valueRatio.denominator.unit",
                "type": "str",
            },
            "component_value_ratio_denominator_code": {
                "fhir_key": "valueRatio.denominator.code",
                "type": "str",
            },
            "component_value_string": {
                "fhir_key": "valueString",
                "type": "str",
            },
            "component_value_boolean": {
                "fhir_key": "valueBoolean",
                "type": "bool",
            },
            "component_value_integer": {
                "fhir_key": "valueInteger",
                "type": "int",
            },
        },
    },
]


class ObservationComponentTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'component' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'component' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('component').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationCategoryCodingTransformer instance with the resource type 'Observation',
            subtype 'category.coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "component", TRANSFORM_SCHEMA)
