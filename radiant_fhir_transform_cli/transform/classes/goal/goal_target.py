"""
FHIR Goal Target transformer
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
            "goal_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "target",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "target_measure_coding": {
                "fhir_key": "measure.coding",
                "type": "str",
            },
            "target_measure_text": {"fhir_key": "measure.text", "type": "str"},
            "target_detail_quantity_value": {
                "fhir_key": "detailQuantity.value",
                "type": "str",
            },
            "target_detail_quantity_comparator": {
                "fhir_key": "detailQuantity.comparator",
                "type": "str",
            },
            "target_detail_quantity_unit": {
                "fhir_key": "detailQuantity.unit",
                "type": "str",
            },
            "target_detail_quantity_system": {
                "fhir_key": "detailQuantity.system",
                "type": "str",
            },
            "target_detail_quantity_code": {
                "fhir_key": "detailQuantity.code",
                "type": "str",
            },
            "target_detail_range_low_value": {
                "fhir_key": "detailRange.low.value",
                "type": "str",
            },
            "target_detail_range_low_unit": {
                "fhir_key": "detailRange.low.unit",
                "type": "str",
            },
            "target_detail_range_low_system": {
                "fhir_key": "detailRange.low.system",
                "type": "str",
            },
            "target_detail_range_low_code": {
                "fhir_key": "detailRange.low.code",
                "type": "str",
            },
            "target_detail_range_high_value": {
                "fhir_key": "detailRange.high.value",
                "type": "str",
            },
            "target_detail_range_high_unit": {
                "fhir_key": "detailRange.high.unit",
                "type": "str",
            },
            "target_detail_range_high_system": {
                "fhir_key": "detailRange.high.system",
                "type": "str",
            },
            "target_detail_range_high_code": {
                "fhir_key": "detailRange.high.code",
                "type": "str",
            },
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "target_detail_codeable_concept_coding": {
                "fhir_key": "detailCodeableConcept.coding",
                "type": "str",
            },
            "target_detail_codeable_concept_text": {
                "fhir_key": "detailCodeableConcept.text",
                "type": "str",
            },
            "target_detail_string": {"fhir_key": "detailString", "type": "str"},
            "target_detail_boolean": {
                "fhir_key": "detailBoolean",
                "type": "bool",
            },
            "target_detail_integer": {
                "fhir_key": "detailInteger",
                "type": "int",
            },
            "target_detail_ratio_numerator_value": {
                "fhir_key": "detailRatio.numerator.value",
                "type": "str",
            },
            "target_detail_ratio_numerator_comparator": {
                "fhir_key": "detailRatio.numerator.comparator",
                "type": "str",
            },
            "target_detail_ratio_numerator_unit": {
                "fhir_key": "detailRatio.numerator.unit",
                "type": "str",
            },
            "target_detail_ratio_numerator_system": {
                "fhir_key": "detailRatio.numerator.system",
                "type": "str",
            },
            "target_detail_ratio_numerator_code": {
                "fhir_key": "detailRatio.numerator.code",
                "type": "str",
            },
            "target_detail_ratio_denominator_value": {
                "fhir_key": "detailRatio.denominator.value",
                "type": "str",
            },
            "target_detail_ratio_denominator_comparator": {
                "fhir_key": "detailRatio.denominator.comparator",
                "type": "str",
            },
            "target_detail_ratio_denominator_unit": {
                "fhir_key": "detailRatio.denominator.unit",
                "type": "str",
            },
            "target_detail_ratio_denominator_system": {
                "fhir_key": "detailRatio.denominator.system",
                "type": "str",
            },
            "target_detail_ratio_denominator_code": {
                "fhir_key": "detailRatio.denominator.code",
                "type": "str",
            },
            "target_due_date": {"fhir_key": "dueDate", "type": "datetime"},
            "target_due_duration_value": {
                "fhir_key": "dueDuration.value",
                "type": "str",
            },
            "target_due_duration_unit": {
                "fhir_key": "dueDuration.unit",
                "type": "str",
            },
            "target_due_duration_system": {
                "fhir_key": "dueDuration.system",
                "type": "str",
            },
            "target_due_duration_code": {
                "fhir_key": "dueDuration.code",
                "type": "str",
            },
        },
    },
]


class GoalTargetTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Goal' resource in FHIR, focusing on the 'target' element.

    This class transforms FHIR Goal JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'target' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Goal').
        subtype (str): Specifies the sub-element of the resource to focus on ('target').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the GoalTargetTransformer instance with the resource type 'Goal',
            subtype 'target', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Goal", "target", TRANSFORM_SCHEMA)
