"""
FHIR Observation Component transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_DICT = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "columns": {
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "component.dataAbsentReason",
        "columns": {
            "component_data_absent_reason_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "component_data_absent_reason_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "component_data_absent_reason_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "component.valueQuantity",
        "columns": {
            "component_value_quantity_value": {
                "fhir_key": "value",
                "type": "str",
            },
            "component_value_quantity_unit": {
                "fhir_key": "unit",
                "type": "str",
            },
            "component_value_quantity_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "component_value_quantity_system": {
                "fhir_key": "system",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "component.valueRange",
        "columns": {
            "component_value_range_low_value": {
                "fhir_key": "low.value",
                "type": "str",
            },
            "component_value_range_low_unit": {
                "fhir_key": "low.unit",
                "type": "str",
            },
            "component_value_range_high_value": {
                "fhir_key": "high.value",
                "type": "str",
            },
            "component_value_range_high_unit": {
                "fhir_key": "high.unit",
                "type": "str",
            },
        },
    },
    {
        "fhire_path": "componentvalueRatio",
        "columns": {
            "component_value_ratio_numerator_value": {
                "fhir_key": "numerator.value",
                "type": "str",
            },
            "component_value_ratio_numerator_unit": {
                "fhir_key": "numerator.unit",
                "type": "str",
            },
            "component_value_ratio_numerator_code": {
                "fhir_key": "numerator.code",
                "type": "str",
            },
            "component_value_ratio_denominator_value": {
                "fhir_key": "denominator.value",
                "type": "str",
            },
            "component_value_ratio_denominator_unit": {
                "fhir_key": "denominator.unit",
                "type": "str",
            },
            "component_value_ratio_denominator_code": {
                "fhir_key": "denominator.code",
                "type": "str",
            },
        },
    },
    {
        "fhire_path": "componentvalueString",
        "columns": {
            "component_value_string": {"fhir_key": "valueString", "type": "str"}
        },
    },
    {
        "fhire_path": "componentvalueBoolean",
        "columns": {
            "component_value_boolean": {
                "fhir_key": "valueBoolean",
                "type": "bool",
            },
        },
    },
    {
        "fhire_path": "component.valueInteger",
        "columns": {
            "component_value_integer": {
                "fhir_key": "valueInteger",
                "type": "int",
            }
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
        super().__init__("Observation", "component", TRANSFORM_DICT)
