"""
Test data helper classes
"""

from tests.data.observation import (
    ObservationCategoryCodingTestHelper,
    ObservationTestHelper,
)
from tests.data.patient import PatientTestHelper

test_helpers = {
    # PatientTestHelper.resource_type: PatientTestHelper,
    (
        ObservationTestHelper.resource_type,
        ObservationTestHelper.resource_subtype,
    ): ObservationTestHelper,
    (
        ObservationCategoryCodingTestHelper.resource_type,
        ObservationCategoryCodingTestHelper.resource_subtype,
    ): ObservationCategoryCodingTestHelper,
}
