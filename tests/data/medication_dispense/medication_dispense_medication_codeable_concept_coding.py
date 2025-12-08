"""
Test helper class for FHIR resource type MedicationDispense subtype Medication CodeableConcept Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication_dispense import (
    MedicationDispenseMedicationCodeableConceptCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_dispense_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": None,
        "medication_dispense_id": "meddisp001",
        "medication_codeable_concept_coding_system": "http://hl7.org/fhir/sid/ndc",
        "medication_codeable_concept_coding_code": "76388-713-25",
        "medication_codeable_concept_coding_display": "Myleran 2mg tablet, film coated",
    }
]


class MedicationDispenseMedicationCodeableConceptCodingTestHelper(
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
    resource_subtype = "medication_codeable_concept_coding"
    transformer = MedicationDispenseMedicationCodeableConceptCodingTransformer
    expected_table_name = (
        "medication_dispense_medication_codeable_concept_coding"
    )

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
