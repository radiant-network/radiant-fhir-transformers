"""
Test data helper classes
"""

from tests.data.observation import ObservationTestHelper
from tests.data.patient import PatientTestHelper

test_helpers = {
    PatientTestHelper.resource_type: PatientTestHelper,
    ObservationTestHelper.resource_type: ObservationTestHelper,
}
