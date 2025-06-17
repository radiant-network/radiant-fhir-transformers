"""
Test helper class for FHIR resource type Goal subtype Target
"""

from radiant_fhir_transform_cli.transform.classes.goal import (
    GoalTargetTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .goal_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "goal_id": "example",
        "target_measure_coding": [
            {
                "system": "http://loinc.org",
                "code": "3141-9",
                "display": "Weight Measured",
            }
        ],
        "target_measure_text": None,
        "target_detail_quantity_value": None,
        "target_detail_quantity_comparator": None,
        "target_detail_quantity_unit": None,
        "target_detail_quantity_system": None,
        "target_detail_quantity_code": None,
        "target_detail_range_low_value": 160,
        "target_detail_range_low_unit": "lbs",
        "target_detail_range_low_system": "http://unitsofmeasure.org",
        "target_detail_range_low_code": "[lb_av]",
        "target_detail_range_high_value": 180,
        "target_detail_range_high_unit": "lbs",
        "target_detail_range_high_system": "http://unitsofmeasure.org",
        "target_detail_range_high_code": "[lb_av]",
        "target_detail_codeable_concept_coding": None,
        "target_detail_codeable_concept_text": None,
        "target_detail_string": None,
        "target_detail_boolean": None,
        "target_detail_integer": None,
        "target_detail_ratio_numerator_value": None,
        "target_detail_ratio_numerator_comparator": None,
        "target_detail_ratio_numerator_unit": None,
        "target_detail_ratio_numerator_system": None,
        "target_detail_ratio_numerator_code": None,
        "target_detail_ratio_denominator_value": None,
        "target_detail_ratio_denominator_comparator": None,
        "target_detail_ratio_denominator_unit": None,
        "target_detail_ratio_denominator_system": None,
        "target_detail_ratio_denominator_code": None,
        "target_due_date": "2016-04-05",
        "target_due_duration_value": None,
        "target_due_duration_unit": None,
        "target_due_duration_system": None,
        "target_due_duration_code": None,
    },
]


class GoalTargetTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Goal' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Goal' resource.

    It predefines the resource type as 'Goal'
    and initializes the resource with the specific 'Goal' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Goal'.
        resource (dict): The raw FHIR 'Goal' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Goal' resource payload.
    """

    resource_type = "Goal"
    resource_subtype = "target"
    transformer = GoalTargetTransformer
    expected_table_name = "goal_target"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
