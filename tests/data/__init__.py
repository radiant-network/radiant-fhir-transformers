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
    ServiceRequestBodySiteTestHelper,
    ServiceRequestCategoryTestHelper,
    ServiceRequestCodeCodingTestHelper,
    ServiceRequestContainedTestHelper,
    ServiceRequestIdentifierTestHelper,
    ServiceRequestInstantiatesUriTestHelper,
    ServiceRequestInsuranceTestHelper,
    ServiceRequestLocationCodeTestHelper,
    ServiceRequestLocationReferenceTestHelper,
    ServiceRequestNoteTestHelper,
    ServiceRequestOrderDetailTestHelper,
    ServiceRequestPerformerTestHelper,
    ServiceRequestReasonCodeTestHelper,
    ServiceRequestReasonReferenceTestHelper,
    ServiceRequestRelevantHistoryTestHelper,
    ServiceRequestReplacesTestHelper,
    ServiceRequestSpecimenTestHelper,
    ServiceRequestSupportingInfoTestHelper

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
    ServiceRequestBodySiteTestHelper,
    ServiceRequestCategoryTestHelper,
    ServiceRequestCodeCodingTestHelper,
    ServiceRequestContainedTestHelper,
    ServiceRequestIdentifierTestHelper,
    ServiceRequestInstantiatesUriTestHelper,
    ServiceRequestInsuranceTestHelper,
    ServiceRequestLocationCodeTestHelper,
    ServiceRequestLocationReferenceTestHelper,
    ServiceRequestNoteTestHelper,
    ServiceRequestOrderDetailTestHelper,
    ServiceRequestPerformerTestHelper,
    ServiceRequestReasonCodeTestHelper,
    ServiceRequestReasonReferenceTestHelper,
    ServiceRequestRelevantHistoryTestHelper,
    ServiceRequestReplacesTestHelper,
    ServiceRequestSpecimenTestHelper,
    ServiceRequestSupportingInfoTestHelper
]
