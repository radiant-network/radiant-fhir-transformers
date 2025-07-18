"""
FHIR Observation Component transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
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
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "component_code_coding": {"fhir_key": "code.coding", "type": "str"},
            "component_code_text": {"fhir_key": "code.text", "type": "str"},
            "component_value_quantity_value": {
                "fhir_key": "valueQuantity.value",
                "type": "str",
            },
            "component_value_quantity_comparator": {
                "fhir_key": "valueQuantity.comparator",
                "type": "str",
            },
            "component_value_quantity_unit": {
                "fhir_key": "valueQuantity.unit",
                "type": "str",
            },
            "component_value_quantity_system": {
                "fhir_key": "valueQuantity.system",
                "type": "str",
            },
            "component_value_quantity_code": {
                "fhir_key": "valueQuantity.code",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "component_value_codeable_concept_coding": {
                "fhir_key": "valueCodeableConcept.coding",
                "type": "str",
            },
            "component_value_codeable_concept_text": {
                "fhir_key": "valueCodeableConcept.text",
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
            "component_value_range_low_value": {
                "fhir_key": "valueRange.low.value",
                "type": "str",
            },
            "component_value_range_low_unit": {
                "fhir_key": "valueRange.low.unit",
                "type": "str",
            },
            "component_value_range_low_system": {
                "fhir_key": "valueRange.low.system",
                "type": "str",
            },
            "component_value_range_low_code": {
                "fhir_key": "valueRange.low.code",
                "type": "str",
            },
            "component_value_range_high_value": {
                "fhir_key": "valueRange.high.value",
                "type": "str",
            },
            "component_value_range_high_unit": {
                "fhir_key": "valueRange.high.unit",
                "type": "str",
            },
            "component_value_range_high_system": {
                "fhir_key": "valueRange.high.system",
                "type": "str",
            },
            "component_value_range_high_code": {
                "fhir_key": "valueRange.high.code",
                "type": "str",
            },
            "component_value_ratio_numerator_value": {
                "fhir_key": "valueRatio.numerator.value",
                "type": "str",
            },
            "component_value_ratio_numerator_comparator": {
                "fhir_key": "valueRatio.numerator.comparator",
                "type": "str",
            },
            "component_value_ratio_numerator_unit": {
                "fhir_key": "valueRatio.numerator.unit",
                "type": "str",
            },
            "component_value_ratio_numerator_system": {
                "fhir_key": "valueRatio.numerator.system",
                "type": "str",
            },
            "component_value_ratio_numerator_code": {
                "fhir_key": "valueRatio.numerator.code",
                "type": "str",
            },
            "component_value_ratio_denominator_value": {
                "fhir_key": "valueRatio.denominator.value",
                "type": "str",
            },
            "component_value_ratio_denominator_comparator": {
                "fhir_key": "valueRatio.denominator.comparator",
                "type": "str",
            },
            "component_value_ratio_denominator_unit": {
                "fhir_key": "valueRatio.denominator.unit",
                "type": "str",
            },
            "component_value_ratio_denominator_system": {
                "fhir_key": "valueRatio.denominator.system",
                "type": "str",
            },
            "component_value_ratio_denominator_code": {
                "fhir_key": "valueRatio.denominator.code",
                "type": "str",
            },
            "component_value_sampled_data_origin_value": {
                "fhir_key": "valueSampledData.origin.value",
                "type": "str",
            },
            "component_value_sampled_data_origin_unit": {
                "fhir_key": "valueSampledData.origin.unit",
                "type": "str",
            },
            "component_value_sampled_data_origin_system": {
                "fhir_key": "valueSampledData.origin.system",
                "type": "str",
            },
            "component_value_sampled_data_origin_code": {
                "fhir_key": "valueSampledData.origin.code",
                "type": "str",
            },
            "component_value_sampled_data_period": {
                "fhir_key": "valueSampledData.period",
                "type": "str",
            },
            "component_value_sampled_data_factor": {
                "fhir_key": "valueSampledData.factor",
                "type": "str",
            },
            "component_value_sampled_data_lower_limit": {
                "fhir_key": "valueSampledData.lowerLimit",
                "type": "str",
            },
            "component_value_sampled_data_upper_limit": {
                "fhir_key": "valueSampledData.upperLimit",
                "type": "str",
            },
            "component_value_sampled_data_dimensions": {
                "fhir_key": "valueSampledData.dimensions",
                "type": "int",
            },
            "component_value_sampled_data_data": {
                "fhir_key": "valueSampledData.data",
                "type": "str",
            },
            "component_value_time": {"fhir_key": "valueTime", "type": "str"},
            "component_value_date_time": {
                "fhir_key": "valueDateTime",
                "type": "datetime",
            },
            "component_value_period_start": {
                "fhir_key": "valuePeriod.start",
                "type": "datetime",
            },
            "component_value_period_end": {
                "fhir_key": "valuePeriod.end",
                "type": "datetime",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "component_data_absent_reason_coding": {
                "fhir_key": "dataAbsentReason.coding",
                "type": "str",
            },
            "component_data_absent_reason_text": {
                "fhir_key": "dataAbsentReason.text",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "component_interpretation": {
                "fhir_key": "interpretation",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "component_reference_range": {
                "fhir_key": "referenceRange",
                "type": "str",
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
            Initializes the ObservationComponentTransformer instance with the resource type 'Observation',
            subtype 'component', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "component", TRANSFORM_SCHEMA)
