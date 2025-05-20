"""
List of FHIR ndjson to dict transformers
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceAuthorTransformer,
    DocumentReferenceContentTransformer,
    DocumentReferenceIdentifierTransformer,
    DocumentReferenceTransformer,
    DocumentReferenceTypeCodingTransformer,
)
from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationBasedOnTransformer,
    ObservationCategoryCodingTransformer,
    ObservationComponentTransformer,
    ObservationExtensionTransformer,
    ObservationNoteTransformer,
    ObservationPerformerTransformer,
    ObservationTransformer,
    ObservationValueCodeableConceptCodingTransformer,
)
from radiant_fhir_transform_cli.transform.classes.observation.observation_code_coding import (
    ObservationCodeCodingTransformer,
)
from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientTransformer,
)
from radiant_fhir_transform_cli.transform.classes.medication import (
    MedicationTransformer,
    MedicationIdentifierTransformer,
    MedicationCodeCodingTransformer,
    MedicationFormCodingTransformer,
    MedicationIngredientTransformer,
)
from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestTransformer,
    MedicationRequestIdentifierTransformer,
    MedicationRequestStatusReasonCodingTransformer,
    MedicationRequestCategoryTransformer,
    MedicationRequestMedicationCodeableConceptCodingTransformer,
    MedicationRequestSupportingInformationTransformer,
    MedicationRequestPerformerTypeCodingTransformer,
    MedicationRequestReasonCodeTransformer,
    MedicationRequestReasonReferenceTransformer,
    MedicationRequestInstantiatesCanonicalTransformer,
    MedicationRequestInstantiatesUriTransformer,
    MedicationRequestBasedOnTransformer,
    MedicationRequestCourseOfTherapyTypeCodingTransformer,
    MedicationRequestInsuranceTransformer,
    MedicationRequestNoteTransformer,
    MedicationRequestDosageInstructionTransformer,
    MedicationRequestSubstitutionAllowedCodeableConceptCodingTransformer,
    MedicationRequestSubstitutionReasonCodingTransformer,
    MedicationRequestDetectedIssueTransformer,
    MedicationRequestEventHistoryTransformer,
)

from radiant_fhir_transform_cli.transform.classes.specimen import (
    SpecimenTransformer,
    SpecimenCollectionBodySiteCodingTransformer,
    SpecimenCollectionFastingStatusCodeableConceptCodingTransformer,
    SpecimenTypeCodingTransformer,
    SpecimenConditionTransformer,
    SpecimenContainerTransformer,
    SpecimenCollectionMethodCodingTransformer,
    SpecimenParentTransformer,
    SpecimenProcessingTransformer,
    SpecimenRequestTransformer,
    SpecimenNoteTransformer,
)

from radiant_fhir_transform_cli.transform.classes.diagnostic_report import (
    DiagnosticReportIdentifierTransformer,
    DiagnosticReportTransformer,
)

# Map FHIR resource type to its transformer class
transformers = {
    "Patient": [PatientTransformer],
    "Observation": [
        ObservationTransformer,
        ObservationCategoryCodingTransformer,
        ObservationCodeCodingTransformer,
        ObservationComponentTransformer,
        ObservationExtensionTransformer,
        ObservationNoteTransformer,
        ObservationPerformerTransformer,
        ObservationValueCodeableConceptCodingTransformer,
        ObservationBasedOnTransformer,
    ],
    "DocumentReference": [
        DocumentReferenceTransformer,
        DocumentReferenceContentTransformer,
        DocumentReferenceTypeCodingTransformer,
        DocumentReferenceIdentifierTransformer,
        DocumentReferenceAuthorTransformer,
    ],
    "Medication": [
        MedicationTransformer,
        MedicationIdentifierTransformer,
        MedicationCodeCodingTransformer,
        MedicationFormCodingTransformer,
        MedicationIngredientTransformer,
    ],
    "Specimen": [
        SpecimenTransformer,
        SpecimenCollectionBodySiteCodingTransformer,
        SpecimenCollectionFastingStatusCodeableConceptCodingTransformer,
        SpecimenTypeCodingTransformer,
        SpecimenConditionTransformer,
        SpecimenContainerTransformer,
        SpecimenCollectionMethodCodingTransformer,
        SpecimenParentTransformer,
        SpecimenProcessingTransformer,
        SpecimenRequestTransformer,
        SpecimenNoteTransformer,
    ],
    "MedicationRequest": [
        MedicationRequestTransformer,
        MedicationRequestIdentifierTransformer,
        MedicationRequestStatusReasonCodingTransformer,
        MedicationRequestCategoryTransformer,
        MedicationRequestMedicationCodeableConceptCodingTransformer,
        MedicationRequestSupportingInformationTransformer,
        MedicationRequestPerformerTypeCodingTransformer,
        MedicationRequestReasonCodeTransformer,
        MedicationRequestReasonReferenceTransformer,
        MedicationRequestInstantiatesCanonicalTransformer,
        MedicationRequestInstantiatesUriTransformer,
        MedicationRequestBasedOnTransformer,
        MedicationRequestCourseOfTherapyTypeCodingTransformer,
        MedicationRequestInsuranceTransformer,
        MedicationRequestNoteTransformer,
        MedicationRequestDosageInstructionTransformer,
        MedicationRequestSubstitutionAllowedCodeableConceptCodingTransformer,
        MedicationRequestSubstitutionReasonCodingTransformer,
        MedicationRequestDetectedIssueTransformer,
        MedicationRequestEventHistoryTransformer,
    ],
    "DiagnosticReport": [
        DiagnosticReportIdentifierTransformer,
        DiagnosticReportTransformer,
    ]
}
