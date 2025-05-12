"""
Test data helper classes
"""

from tests.data.document_reference import (
    DocumentReferenceContentTestHelper,
    DocumentReferenceTestHelper,
)
from tests.data.observation import (
    ObservationBasedOnTestHelper,
    ObservationCategoryCodingTestHelper,
    ObservationCodeCodingTestHelper,
    ObservationComponentTestHelper,
    ObservationExtensionTestHelper,
    ObservationNoteTestHelper,
    ObservationPerformerTestHelper,
    ObservationTestHelper,
    ObservationValueCodeableConceptCodingTestHelper,
)
from tests.data.patient import PatientTestHelper

from tests.data.service_request import (
    ServiceRequestTestHelper,
    ServiceRequestBasedOnTestHelper,
)

test_helpers = [
    PatientTestHelper,
    ObservationTestHelper,
    ObservationCategoryCodingTestHelper,
    ObservationCodeCodingTestHelper,
    ObservationComponentTestHelper,
    ObservationExtensionTestHelper,
    ObservationNoteTestHelper,
    ObservationPerformerTestHelper,
    ObservationValueCodeableConceptCodingTestHelper,
    ObservationBasedOnTestHelper,
    DocumentReferenceTestHelper,
    DocumentReferenceContentTestHelper,
    ServiceRequestTestHelper,
    ServiceRequestBasedOnTestHelper,
]
