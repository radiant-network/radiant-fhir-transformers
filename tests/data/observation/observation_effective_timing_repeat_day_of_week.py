"""
Test helper class for FHIR resource type Observation subtype EffectiveTiming Repeat DayOfWeek
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationEffectiveTimingRepeatDayOfWeekTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE_EFFECTIVE_TIMING as RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "effective_timing_repeat_day_of_week": "mon",
    },
]


class ObservationEffectiveTimingRepeatDayOfWeekTestHelper(
    FhirResourceTestHelper
):
    """
    A helper class for testing transformations of the FHIR 'Observation' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Observation' resource.

    It predefines the resource type as 'Observation'
    and initializes the resource with the specific 'Observation' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Observation'.
        resource (dict): The raw FHIR 'Observation' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Observation' resource payload.
    """

    resource_type = "Observation"
    resource_subtype = "effective_timing_repeat_day_of_week"
    transformer = ObservationEffectiveTimingRepeatDayOfWeekTransformer
    expected_table_name = "observation_effective_timing_repeat_day_of_week"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
