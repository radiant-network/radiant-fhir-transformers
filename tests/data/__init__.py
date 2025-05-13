"""
Test data helper classes
"""

from tests.data.document_reference import (
    DocumentReferenceAuthorTestHelper,
    DocumentReferenceContentTestHelper,
    DocumentReferenceIdentifierTestHelper,
    DocumentReferenceTestHelper,
    DocumentReferenceTypeCodingTestHelper,
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
from tests.data.medication import (
    MedicationTestHelper,
    MedicationIdentifierTestHelper,
    MedicationCodeCodingTestHelper,
    MedicationFormCodingTestHelper,
    MedicationIngredientTestHelper,
)
from tests.data.specimen import(
    SpecimenTestHelper,
    SpecimenCollectionBodySiteCodingTestHelper,
    SpecimenCollectionFastingStatusCodeableConceptCodingTestHelper,
    SpecimenCollectionMethodCodingTestHelper,
    SpecimenConditionTestHelper,
    SpecimenContainerTestHelper,
    SpecimenNoteTestHelper,
    SpecimenParentTestHelper,
    SpecimenRequestTestHelper,
    SpecimenProcessingTestHelper,
    SpecimenTypeCodingTestHelper
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
    DocumentReferenceTypeCodingTestHelper,
    DocumentReferenceIdentifierTestHelper,
    DocumentReferenceAuthorTestHelper,
    MedicationTestHelper,
    MedicationIdentifierTestHelper,
    MedicationCodeCodingTestHelper,
    MedicationFormCodingTestHelper,
    MedicationIngredientTestHelper,
    SpecimenTestHelper,
    SpecimenCollectionBodySiteCodingTestHelper,
    SpecimenCollectionFastingStatusCodeableConceptCodingTestHelper,
    SpecimenCollectionMethodCodingTestHelper,
    SpecimenConditionTestHelper,
    SpecimenContainerTestHelper,
    SpecimenNoteTestHelper,
    SpecimenParentTestHelper,
    SpecimenRequestTestHelper,
    SpecimenProcessingTestHelper,
    SpecimenTypeCodingTestHelper
]
