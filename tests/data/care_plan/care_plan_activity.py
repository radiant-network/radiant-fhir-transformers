"""
Test helper class for FHIR resource type CarePlan subtype Activity
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanActivityTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "care_plan_id": "preg",
        "activity_outcome_codeable_concept": None,
        "activity_outcome_reference": None,
        "activity_outcome_progress": None,
        "activity_reference_reference": None,
        "activity_reference.display": "Prenatal vitamin MedicationRequest",
        "activity_reference.type": None,
        "activity_detail_kind": None,
        "activity_detail_instantiates_canonical": None,
        "activity_detail_instantiates_uri": None,
        "activity_detail_code_coding": None,
        "activity_detail_code_text": None,
        "activity_detail_reason_code": None,
        "activity_detail_reason_reference": None,
        "activity_detail_goal": None,
        "activity_detail_status": None,
        "activity_detail_status_reason": None,
        "activity_detail_do_not_perform": None,
        # start Scheduled element
        # scheduledTiming
        "activity_detail_scheduled_timing_event": None,
        # scheduledTiming.repeat.boundsDuration
        "activity_detail_scheduled_timing_repeat_bounds_duration_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_comparator": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_code": None,
        # scheduledTiming.repeat.boundsRange
        "activity_detail_scheduled_timing_repeat_bounds_range_low_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_code": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_code": None,
        # scheduledTiming.repeat.boundsPeriod
        "activity_detail_scheduled_timing_repeat_bounds_period_start": None,
        "activity_detail_scheduled_timing_repeat_bounds_period_end": None,
        # scheduledTiming.repeat
        "activity_detail_scheduled_timing_repeat_count": None,
        "activity_detail_scheduled_timing_repeat_count_max": None,
        "activity_detail_scheduled_timing_repeat_duration": None,
        "activity_detail_scheduled_timing_repeat_duration_max": None,
        "activity_detail_scheduled_timing_repeat_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_frequency": None,
        "activity_detail_scheduled_timing_repeat_frequency_max": None,
        "activity_detail_scheduled_timing_repeat_period": None,
        "activity_detail_scheduled_timing_repeat_period_max": None,
        "activity_detail_scheduled_timing_repeat_period_unit": None,
        "activity_detail_scheduled_timing_repeat_day_of_week": None,
        "activity_detail_scheduled_timing_repeat_time_of_day": None,
        "activity_detail_scheduled_timing_repeat_when": None,
        "activity_detail_scheduled_timing_repeat_offset": None,
        "activity_detail_scheduled_timing_code": None,
        # scheduledPeriod
        "activity_detail_scheduled_period_start": None,
        "activity_detail_scheduled_period_end": None,
        # scheduledString
        "activity_detail_scheduled_string": None,
        # end Scheduled element
        "activity_detail_location_reference": None,
        "activity_detail_location_type": None,
        "activity_detail_location_display": None,
        "activity_detail_performer": None,
        "activity_detail_product_codeable_concept_text": None,
        "activity_detail_product_codeable_concept_coding": None,
        "activity_detail_product_reference_reference": None,
        "activity_detail_product_reference_display": None,
        "activity_detail_product_reference_type": None,
        "activity_detail_daily_amount_value": None,
        "activity_detail_daily_amount_unit": None,
        "activity_detail_daily_amount_system": None,
        "activity_detail_daily_amount_code": None,
        "activity_detail_quantity_value": None,
        "activity_detail_quantity_unit": None,
        "activity_detail_quantity_system": None,
        "activity_detail_quantity_code": None,
        "activity_detail_description": None,
    },
    {
        "care_plan_id": "preg",
        "activity_outcome_codeable_concept": None,
        "activity_outcome_reference": None,
        "activity_outcome_progress": None,
        "activity_reference_reference": None,
        "activity_reference.display": None,
        "activity_reference.type": None,
        "activity_detail_kind": "Appointment",
        "activity_detail_instantiates_canonical": None,
        "activity_detail_instantiates_uri": None,
        "activity_detail_code_coding": [
            {"system": "http://example.org/mySystem", "code": "1an"}
        ],
        "activity_detail_code_text": "First Antenatal encounter",
        "activity_detail_reason_code": None,
        "activity_detail_reason_reference": None,
        "activity_detail_goal": None,
        "activity_detail_status": "scheduled",
        "activity_detail_status_reason": None,
        "activity_detail_do_not_perform": False,
        # start Scheduled element
        # scheduledTiming
        "activity_detail_scheduled_timing_event": None,
        # scheduledTiming.repeat.boundsDuration
        "activity_detail_scheduled_timing_repeat_bounds_duration_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_comparator": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_code": None,
        # scheduledTiming.repeat.boundsRange
        "activity_detail_scheduled_timing_repeat_bounds_range_low_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_code": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_code": None,
        # scheduledTiming.repeat.boundsPeriod
        "activity_detail_scheduled_timing_repeat_bounds_period_start": "2013-02-14",
        "activity_detail_scheduled_timing_repeat_bounds_period_end": "2013-02-28",
        # scheduledTiming.repeat
        "activity_detail_scheduled_timing_repeat_count": None,
        "activity_detail_scheduled_timing_repeat_count_max": None,
        "activity_detail_scheduled_timing_repeat_duration": None,
        "activity_detail_scheduled_timing_repeat_duration_max": None,
        "activity_detail_scheduled_timing_repeat_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_frequency": None,
        "activity_detail_scheduled_timing_repeat_frequency_max": None,
        "activity_detail_scheduled_timing_repeat_period": None,
        "activity_detail_scheduled_timing_repeat_period_max": None,
        "activity_detail_scheduled_timing_repeat_period_unit": None,
        "activity_detail_scheduled_timing_repeat_day_of_week": None,
        "activity_detail_scheduled_timing_repeat_time_of_day": None,
        "activity_detail_scheduled_timing_repeat_when": None,
        "activity_detail_scheduled_timing_repeat_offset": None,
        "activity_detail_scheduled_timing_code": None,
        # scheduledPeriod
        "activity_detail_scheduled_period_start": None,
        "activity_detail_scheduled_period_end": None,
        # scheduledString
        "activity_detail_scheduled_string": None,
        # end Scheduled element
        "activity_detail_location_reference": None,
        "activity_detail_location_type": None,
        "activity_detail_location_display": None,
        "activity_detail_performer": [
            {"reference": "#pr1", "display": "Mavis Midwife"}
        ],
        "activity_detail_product_codeable_concept_text": None,
        "activity_detail_product_codeable_concept_coding": None,
        "activity_detail_product_reference_reference": None,
        "activity_detail_product_reference_display": None,
        "activity_detail_product_reference_type": None,
        "activity_detail_daily_amount_value": None,
        "activity_detail_daily_amount_unit": None,
        "activity_detail_daily_amount_system": None,
        "activity_detail_daily_amount_code": None,
        "activity_detail_quantity_value": None,
        "activity_detail_quantity_unit": None,
        "activity_detail_quantity_system": None,
        "activity_detail_quantity_code": None,
        "activity_detail_description": "The first antenatal encounter. This is where a detailed physical examination is performed.             and the pregnanacy discussed with the mother-to-be.",
    },
    {
        "care_plan_id": "preg",
        "activity_outcome_codeable_concept": None,
        "activity_outcome_reference": None,
        "activity_outcome_progress": None,
        "activity_reference_reference": None,
        "activity_reference.display": None,
        "activity_reference.type": None,
        "activity_detail_kind": "Appointment",
        "activity_detail_instantiates_canonical": None,
        "activity_detail_instantiates_uri": None,
        "activity_detail_code_coding": [
            {"system": "http://example.org/mySystem", "code": "an"}
        ],
        "activity_detail_code_text": "Follow-up Antenatal encounter",
        "activity_detail_reason_code": None,
        "activity_detail_reason_reference": None,
        "activity_detail_goal": None,
        "activity_detail_status": "not-started",
        "activity_detail_status_reason": None,
        "activity_detail_do_not_perform": False,
        # start Scheduled element
        # scheduledTiming
        "activity_detail_scheduled_timing_event": None,
        # scheduledTiming.repeat.boundsDuration
        "activity_detail_scheduled_timing_repeat_bounds_duration_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_comparator": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_code": None,
        # scheduledTiming.repeat.boundsRange
        "activity_detail_scheduled_timing_repeat_bounds_range_low_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_code": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_code": None,
        # scheduledTiming.repeat.boundsPeriod
        "activity_detail_scheduled_timing_repeat_bounds_period_start": "2013-03-01",
        "activity_detail_scheduled_timing_repeat_bounds_period_end": "2013-03-14",
        # scheduledTiming.repeat
        "activity_detail_scheduled_timing_repeat_count": None,
        "activity_detail_scheduled_timing_repeat_count_max": None,
        "activity_detail_scheduled_timing_repeat_duration": None,
        "activity_detail_scheduled_timing_repeat_duration_max": None,
        "activity_detail_scheduled_timing_repeat_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_frequency": None,
        "activity_detail_scheduled_timing_repeat_frequency_max": None,
        "activity_detail_scheduled_timing_repeat_period": None,
        "activity_detail_scheduled_timing_repeat_period_max": None,
        "activity_detail_scheduled_timing_repeat_period_unit": None,
        "activity_detail_scheduled_timing_repeat_day_of_week": None,
        "activity_detail_scheduled_timing_repeat_time_of_day": None,
        "activity_detail_scheduled_timing_repeat_when": None,
        "activity_detail_scheduled_timing_repeat_offset": None,
        "activity_detail_scheduled_timing_code": None,
        # scheduledPeriod
        "activity_detail_scheduled_period_start": None,
        "activity_detail_scheduled_period_end": None,
        # scheduledString
        "activity_detail_scheduled_string": None,
        # end Scheduled element
        "activity_detail_location_reference": None,
        "activity_detail_location_type": None,
        "activity_detail_location_display": None,
        "activity_detail_performer": [
            {"reference": "#pr1", "display": "Mavis Midwife"}
        ],
        "activity_detail_product_codeable_concept_text": None,
        "activity_detail_product_codeable_concept_coding": None,
        "activity_detail_product_reference_reference": None,
        "activity_detail_product_reference_display": None,
        "activity_detail_product_reference_type": None,
        "activity_detail_daily_amount_value": None,
        "activity_detail_daily_amount_unit": None,
        "activity_detail_daily_amount_system": None,
        "activity_detail_daily_amount_code": None,
        "activity_detail_quantity_value": None,
        "activity_detail_quantity_unit": None,
        "activity_detail_quantity_system": None,
        "activity_detail_quantity_code": None,
        "activity_detail_description": "The second antenatal encounter. Discuss any issues that arose from the first antenatal encounter",
    },
    {
        "care_plan_id": "preg",
        "activity_outcome_codeable_concept": None,
        "activity_outcome_reference": None,
        "activity_outcome_progress": None,
        "activity_reference_reference": None,
        "activity_reference.display": None,
        "activity_reference.type": None,
        "activity_detail_kind": "Appointment",
        "activity_detail_instantiates_canonical": None,
        "activity_detail_instantiates_uri": None,
        "activity_detail_code_coding": [
            {"system": "http://example.org/mySystem", "code": "del"}
        ],
        "activity_detail_code_text": "Delivery",
        "activity_detail_reason_code": None,
        "activity_detail_reason_reference": None,
        "activity_detail_goal": None,
        "activity_detail_status": "not-started",
        "activity_detail_status_reason": None,
        "activity_detail_do_not_perform": False,
        # start Scheduled element
        # scheduledTiming
        "activity_detail_scheduled_timing_event": None,
        # scheduledTiming.repeat.boundsDuration
        "activity_detail_scheduled_timing_repeat_bounds_duration_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_comparator": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_duration_code": None,
        # scheduledTiming.repeat.boundsRange
        "activity_detail_scheduled_timing_repeat_bounds_range_low_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_low_code": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_value": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_unit": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_system": None,
        "activity_detail_scheduled_timing_repeat_bounds_range_high_code": None,
        # scheduledTiming.repeat.boundsPeriod
        "activity_detail_scheduled_timing_repeat_bounds_period_start": "2013-09-01",
        "activity_detail_scheduled_timing_repeat_bounds_period_end": "2013-09-14",
        # scheduledTiming.repeat
        "activity_detail_scheduled_timing_repeat_count": None,
        "activity_detail_scheduled_timing_repeat_count_max": None,
        "activity_detail_scheduled_timing_repeat_duration": None,
        "activity_detail_scheduled_timing_repeat_duration_max": None,
        "activity_detail_scheduled_timing_repeat_duration_unit": None,
        "activity_detail_scheduled_timing_repeat_frequency": None,
        "activity_detail_scheduled_timing_repeat_frequency_max": None,
        "activity_detail_scheduled_timing_repeat_period": None,
        "activity_detail_scheduled_timing_repeat_period_max": None,
        "activity_detail_scheduled_timing_repeat_period_unit": None,
        "activity_detail_scheduled_timing_repeat_day_of_week": None,
        "activity_detail_scheduled_timing_repeat_time_of_day": None,
        "activity_detail_scheduled_timing_repeat_when": None,
        "activity_detail_scheduled_timing_repeat_offset": None,
        "activity_detail_scheduled_timing_code": None,
        # scheduledPeriod
        "activity_detail_scheduled_period_start": None,
        "activity_detail_scheduled_period_end": None,
        # scheduledString
        "activity_detail_scheduled_string": None,
        # end Scheduled element
        "activity_detail_location_reference": None,
        "activity_detail_location_type": None,
        "activity_detail_location_display": None,
        "activity_detail_performer": [
            {"reference": "#pr1", "display": "Mavis Midwife"}
        ],
        "activity_detail_product_codeable_concept_text": None,
        "activity_detail_product_codeable_concept_coding": None,
        "activity_detail_product_reference_reference": None,
        "activity_detail_product_reference_display": None,
        "activity_detail_product_reference_type": None,
        "activity_detail_daily_amount_value": None,
        "activity_detail_daily_amount_unit": None,
        "activity_detail_daily_amount_system": None,
        "activity_detail_daily_amount_code": None,
        "activity_detail_quantity_value": None,
        "activity_detail_quantity_unit": None,
        "activity_detail_quantity_system": None,
        "activity_detail_quantity_code": None,
        "activity_detail_description": "The delivery.",
    },
]


class CarePlanActivityTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'CarePlan' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'CarePlan' resource.

    It predefines the resource type as 'CarePlan'
    and initializes the resource with the specific 'CarePlan' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'CarePlan'.

        resource (dict): The raw FHIR 'CarePlan' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'CarePlan' resource payload.
    """

    resource_type = "CarePlan"
    resource_subtype = "activity"
    transformer = CarePlanActivityTransformer
    expected_table_name = "care_plan_activity"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
