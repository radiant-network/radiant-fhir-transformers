"""FHIR Goal target transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Goal",
    "name": "goal_target",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "goal_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "target",
            "column": [
                {
                    "name": "target_measure_text",
                    "path": "measure.text",
                    "type": "string",
                },
                {
                    "name": "target_detail_quantity_value",
                    "path": "detailQuantity.value",
                    "type": "string",
                },
                {
                    "name": "target_detail_quantity_comparator",
                    "path": "detailQuantity.comparator",
                    "type": "string",
                },
                {
                    "name": "target_detail_quantity_unit",
                    "path": "detailQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "target_detail_quantity_system",
                    "path": "detailQuantity.system",
                    "type": "string",
                },
                {
                    "name": "target_detail_quantity_code",
                    "path": "detailQuantity.code",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_low_value",
                    "path": "detailRange.low.value",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_low_unit",
                    "path": "detailRange.low.unit",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_low_system",
                    "path": "detailRange.low.system",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_low_code",
                    "path": "detailRange.low.code",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_high_value",
                    "path": "detailRange.high.value",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_high_unit",
                    "path": "detailRange.high.unit",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_high_system",
                    "path": "detailRange.high.system",
                    "type": "string",
                },
                {
                    "name": "target_detail_range_high_code",
                    "path": "detailRange.high.code",
                    "type": "string",
                },
                {
                    "name": "target_detail_codeable_concept_coding",
                    "path": "detailCodeableConcept.coding",
                    "type": "string",
                },
                {
                    "name": "target_detail_codeable_concept_text",
                    "path": "detailCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "target_detail_string",
                    "path": "detailString",
                    "type": "string",
                },
                {
                    "name": "target_detail_boolean",
                    "path": "detailBoolean",
                    "type": "string",
                },
                {
                    "name": "target_detail_integer",
                    "path": "detailInteger",
                    "type": "integer",
                },
                {
                    "name": "target_detail_ratio_numerator_value",
                    "path": "detailRatio.numerator.value",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_numerator_comparator",
                    "path": "detailRatio.numerator.comparator",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_numerator_unit",
                    "path": "detailRatio.numerator.unit",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_numerator_system",
                    "path": "detailRatio.numerator.system",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_numerator_code",
                    "path": "detailRatio.numerator.code",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_denominator_value",
                    "path": "detailRatio.denominator.value",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_denominator_comparator",
                    "path": "detailRatio.denominator.comparator",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_denominator_unit",
                    "path": "detailRatio.denominator.unit",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_denominator_system",
                    "path": "detailRatio.denominator.system",
                    "type": "string",
                },
                {
                    "name": "target_detail_ratio_denominator_code",
                    "path": "detailRatio.denominator.code",
                    "type": "string",
                },
                {
                    "name": "target_due_date",
                    "path": "dueDate",
                    "type": "dateTime",
                },
                {
                    "name": "target_due_duration_value",
                    "path": "dueDuration.value",
                    "type": "string",
                },
                {
                    "name": "target_due_duration_unit",
                    "path": "dueDuration.unit",
                    "type": "string",
                },
                {
                    "name": "target_due_duration_system",
                    "path": "dueDuration.system",
                    "type": "string",
                },
                {
                    "name": "target_due_duration_code",
                    "path": "dueDuration.code",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEachOrNull": "measure.coding",
                    "column": [
                        {
                            "name": "target_measure_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "target_measure_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                        {
                            "name": "target_measure_coding_display",
                            "path": "display",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class GoalTargetTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Goal", "target", VIEW_DEFINITION)
