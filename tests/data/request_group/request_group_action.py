"""
Test helper class for FHIR resource type RequestGroup subtype Action
"""

from radiant_fhir_transform_cli.transform.classes.request_group import (
    RequestGroupActionTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .request_group_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "action_action": {
            "id": "medication-action-1",
            "description": "Administer medication 1",
            "type": {
                "coding": [
                    {
                        "code": "create",
                    },
                ],
            },
            "resource": {
                "reference": "#medicationrequest-1",
            },
        },
        "action_participant": {
            "reference": "Practitioner/1",
        },
        "action_prefix": "1",
        "action_title": "Administer Medications",
        "action_description": "Administer medications at the appropriate time",
        "action_text_equivalent": "Administer medication 1, followed an hour later by medication 2",
        "action_priority": None,
        "action_code": None,
        "action_documentation": None,
        "action_condition": None,
        "action_related_action": None,
        "action_timing_date_time": "2017-03-06T19:00:00Z",
        "action_timing_age_value": None,
        "action_timing_age_comparator": None,
        "action_timing_age_unit": None,
        "action_timing_age_system": None,
        "action_timing_age_code": None,
        "action_timing_period_start": None,
        "action_timing_period_end": None,
        "action_timing_duration_value": None,
        "action_timing_duration_comparator": None,
        "action_timing_duration_unit": None,
        "action_timing_duration_system": None,
        "action_timing_duration_code": None,
        "action_timing_range_low_value": None,
        "action_timing_range_low_unit": None,
        "action_timing_range_low_system": None,
        "action_timing_range_low_code": None,
        "action_timing_range_high_value": None,
        "action_timing_range_high_unit": None,
        "action_timing_range_high_system": None,
        "action_timing_range_high_code": None,
        "action_timing_timing_event": None,
        "action_timing_timing_repeat_bounds_duration_value": None,
        "action_timing_timing_repeat_bounds_duration_comparator": None,
        "action_timing_timing_repeat_bounds_duration_unit": None,
        "action_timing_timing_repeat_bounds_duration_system": None,
        "action_timing_timing_repeat_bounds_duration_code": None,
        "action_timing_timing_repeat_bounds_range_low_value": None,
        "action_timing_timing_repeat_bounds_range_low_unit": None,
        "action_timing_timing_repeat_bounds_range_low_system": None,
        "action_timing_timing_repeat_bounds_range_low_code": None,
        "action_timing_timing_repeat_bounds_range_high_value": None,
        "action_timing_timing_repeat_bounds_range_high_unit": None,
        "action_timing_timing_repeat_bounds_range_high_system": None,
        "action_timing_timing_repeat_bounds_range_high_code": None,
        "action_timing_timing_repeat_bounds_period_start": None,
        "action_timing_timing_repeat_bounds_period_end": None,
        "action_timing_timing_repeat_count": None,
        "action_timing_timing_repeat_count_max": None,
        "action_timing_timing_repeat_duration": None,
        "action_timing_timing_repeat_duration_max": None,
        "action_timing_timing_repeat_duration_unit": None,
        "action_timing_timing_repeat_frequency": None,
        "action_timing_timing_repeat_frequency_max": None,
        "action_timing_timing_repeat_period": None,
        "action_timing_timing_repeat_period_max": None,
        "action_timing_timing_repeat_period_unit": None,
        "action_timing_timing_repeat_day_of_week": None,
        "action_timing_timing_repeat_time_of_day": None,
        "action_timing_timing_repeat_when": None,
        "action_timing_timing_repeat_offset": None,
        "action_timing_timing_code": None,
        "action_type_coding": None,
        "action_type_text": None,
        "action_grouping_behavior": "logical-group",
        "action_selection_behavior": "all",
        "action_required_behavior": "must",
        "action_precheck_behavior": "yes",
        "action_cardinality_behavior": "single",
        "action_resource_reference": None,
        "action_resource_type": None,
        "action_resource_display": None,
        "id": "9dd65560-b765-4711-986a-cfd41fe9e1b1",
        "request_group_id": "kdn5-example",
    },
    {
        "action_action": {
            "id": "medication-action-2",
            "description": "Administer medication 2",
            "relatedAction": [
                {
                    "actionId": "medication-action-1",
                    "relationship": "after-end",
                    "offsetDuration": {
                        "value": 1,
                        "unit": "h",
                    },
                },
            ],
            "type": {
                "coding": [
                    {
                        "code": "create",
                    },
                ],
            },
            "resource": {
                "reference": "#medicationrequest-2",
            },
        },
        "action_participant": {
            "reference": "Practitioner/1",
        },
        "action_prefix": "1",
        "action_title": "Administer Medications",
        "action_description": "Administer medications at the appropriate time",
        "action_text_equivalent": "Administer medication 1, followed an hour later by medication 2",
        "action_priority": None,
        "action_code": None,
        "action_documentation": None,
        "action_condition": None,
        "action_related_action": None,
        "action_timing_date_time": "2017-03-06T19:00:00Z",
        "action_timing_age_value": None,
        "action_timing_age_comparator": None,
        "action_timing_age_unit": None,
        "action_timing_age_system": None,
        "action_timing_age_code": None,
        "action_timing_period_start": None,
        "action_timing_period_end": None,
        "action_timing_duration_value": None,
        "action_timing_duration_comparator": None,
        "action_timing_duration_unit": None,
        "action_timing_duration_system": None,
        "action_timing_duration_code": None,
        "action_timing_range_low_value": None,
        "action_timing_range_low_unit": None,
        "action_timing_range_low_system": None,
        "action_timing_range_low_code": None,
        "action_timing_range_high_value": None,
        "action_timing_range_high_unit": None,
        "action_timing_range_high_system": None,
        "action_timing_range_high_code": None,
        "action_timing_timing_event": None,
        "action_timing_timing_repeat_bounds_duration_value": None,
        "action_timing_timing_repeat_bounds_duration_comparator": None,
        "action_timing_timing_repeat_bounds_duration_unit": None,
        "action_timing_timing_repeat_bounds_duration_system": None,
        "action_timing_timing_repeat_bounds_duration_code": None,
        "action_timing_timing_repeat_bounds_range_low_value": None,
        "action_timing_timing_repeat_bounds_range_low_unit": None,
        "action_timing_timing_repeat_bounds_range_low_system": None,
        "action_timing_timing_repeat_bounds_range_low_code": None,
        "action_timing_timing_repeat_bounds_range_high_value": None,
        "action_timing_timing_repeat_bounds_range_high_unit": None,
        "action_timing_timing_repeat_bounds_range_high_system": None,
        "action_timing_timing_repeat_bounds_range_high_code": None,
        "action_timing_timing_repeat_bounds_period_start": None,
        "action_timing_timing_repeat_bounds_period_end": None,
        "action_timing_timing_repeat_count": None,
        "action_timing_timing_repeat_count_max": None,
        "action_timing_timing_repeat_duration": None,
        "action_timing_timing_repeat_duration_max": None,
        "action_timing_timing_repeat_duration_unit": None,
        "action_timing_timing_repeat_frequency": None,
        "action_timing_timing_repeat_frequency_max": None,
        "action_timing_timing_repeat_period": None,
        "action_timing_timing_repeat_period_max": None,
        "action_timing_timing_repeat_period_unit": None,
        "action_timing_timing_repeat_day_of_week": None,
        "action_timing_timing_repeat_time_of_day": None,
        "action_timing_timing_repeat_when": None,
        "action_timing_timing_repeat_offset": None,
        "action_timing_timing_code": None,
        "action_type_coding": None,
        "action_type_text": None,
        "action_grouping_behavior": "logical-group",
        "action_selection_behavior": "all",
        "action_required_behavior": "must",
        "action_precheck_behavior": "yes",
        "action_cardinality_behavior": "single",
        "action_resource_reference": None,
        "action_resource_type": None,
        "action_resource_display": None,
        "id": "de258b2f-0452-4883-a9cd-38ea6472fbfb",
        "request_group_id": "kdn5-example",
    },
]


class RequestGroupActionTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'RequestGroup' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'RequestGroup' resource.

    It predefines the resource type as 'RequestGroup'
    and initializes the resource with the specific 'RequestGroup' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'RequestGroup'.
        resource (dict): The raw FHIR 'RequestGroup' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'RequestGroup' resource payload.
    """

    resource_type = "RequestGroup"
    resource_subtype = "action"
    transformer = RequestGroupActionTransformer
    expected_table_name = "request_group_action"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
