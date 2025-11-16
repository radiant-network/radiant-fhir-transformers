"""
Test helper class for FHIR resource type MedicationRequest subtype MedicationCodeableConcept Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestMedicationCodeableConceptCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_request_id": "medrx0301",
        "medication_codeable_concept_coding_system": "http://hl7.org/fhir/sid/ndc",
        "medication_codeable_concept_coding_code": "0069-2587-10",
        "medication_codeable_concept_coding_display": "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)",
    }
]


class MedicationRequestMedicationCodeableConceptCodingTestHelper(
    FhirResourceTestHelper
):
    """
    A helper class for testing transformations of the FHIR 'MedicationRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationRequest' resource.

    It predefines the resource type as 'MedicationRequest'
    and initializes the resource with the specific 'MedicationRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationRequest'.

        resource (dict): The raw FHIR 'MedicationRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationRequest' resource payload.
    """

    resource_type = "MedicationRequest"
    resource_subtype = "medication_codeable_concept_coding"
    transformer = MedicationRequestMedicationCodeableConceptCodingTransformer
    expected_table_name = (
        "medication_request_medication_codeable_concept_coding"
    )

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
