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

from radiant_fhir_transform_cli.transform.classes.service_request import (
    ServiceRequestTransformer,
    ServiceRequestCodeCodingTransformer,
    ServiceRequestReasonCodeTransformer,
    ServiceRequestContainedTransformer,
    ServiceRequestIdentifierTransformer,
    ServiceRequestPerformerTransformer,
    ServiceRequestSupportingInfoTransformer,
    ServiceRequestSpecimenTransformer,
    ServiceRequestNoteTransformer,
    ServiceRequestInstantiatesUriTransformer,
    ServiceRequestBasedOnTransformer,
    ServiceRequestReplacesTransformer,
    ServiceRequestCategoryTransformer,
    ServiceRequestOrderDetailTransformer,
    ServiceRequestLocationCodeTransformer,
    ServiceRequestLocationReferenceTransformer,
    ServiceRequestReasonReferenceTransformer,
    ServiceRequestInsuranceTransformer,
    ServiceRequestBodySiteTransformer,
    ServiceRequestRelevantHistoryTransformer,
)

from radiant_fhir_transform_cli.transform.classes.medication import (
    MedicationTransformer,
    MedicationIdentifierTransformer,
    MedicationCodeCodingTransformer,
    MedicationFormCodingTransformer,
    MedicationIngredientTransformer,

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
    "ServiceRequest": [
        ServiceRequestTransformer,
        ServiceRequestCodeCodingTransformer,
        ServiceRequestReasonCodeTransformer,
        ServiceRequestContainedTransformer,
        ServiceRequestIdentifierTransformer,
        ServiceRequestPerformerTransformer,
        ServiceRequestSupportingInfoTransformer,
        ServiceRequestSpecimenTransformer,
        ServiceRequestNoteTransformer,
        ServiceRequestInstantiatesUriTransformer,
        ServiceRequestBasedOnTransformer,
        ServiceRequestReplacesTransformer,
        ServiceRequestCategoryTransformer,
        ServiceRequestOrderDetailTransformer,
        ServiceRequestLocationCodeTransformer,
        ServiceRequestLocationReferenceTransformer,
        ServiceRequestReasonReferenceTransformer,
        ServiceRequestInsuranceTransformer,
        ServiceRequestBodySiteTransformer,
        ServiceRequestRelevantHistoryTransformer,
    ],
}
