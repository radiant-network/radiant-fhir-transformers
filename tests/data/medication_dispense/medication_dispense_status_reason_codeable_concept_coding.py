"""
Test helper class for FHIR resource type MedicationDispense subtype Status Reason CodeableConcept Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseStatusReasonCodeableConceptCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": None,
        "medication_dispense_id": "meddisp001",
        "status_reason_codeable_concept_coding_system": "http://terminology.hl7.org/CodeSystem/medicationdispense-status-reason",
        "status_reason_codeable_concept_coding_code": "refused",
        "status_reason_codeable_concept_coding_display": "Refused",
    }
]


class MedicationDispenseStatusReasonCodeableConceptCodingTestHelper(
    FhirResourceTestHelper
):
    """
    A helper class for testing transformations of the FHIR 'MedicationDispense' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationDispense' resource.

    It predefines the resource type as 'MedicationDispense'
    and initializes the resource with the specific 'MedicationDispense' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationDispense'.

        resource (dict): The raw FHIR 'MedicationDispense' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationDispense' resource payload.
    """

    resource_type = "MedicationDispense"
    resource_subtype = "status_reason_codeable_concept_coding"
    transformer = MedicationDispenseStatusReasonCodeableConceptCodingTransformer
    expected_table_name = (
        "medication_dispense_status_reason_codeable_concept_coding"
    )

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
