"""
Test helper class for FHIR resource type Medication subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication import (
    MedicationCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://hl7.org/fhir/sid/ndc",
        "code_coding_code": "0069-2587-10",
        "code_coding_display": "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)",
        "id": "d8b90840-a741-4cba-a681-faf216628d0d",
        "medication_id": "med0301",
    },
]


class MedicationCodeCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Medication' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Medication' resource.

    It predefines the resource type as 'Medication'
    and initializes the resource with the specific 'Medication' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Medication'.

        resource (dict): The raw FHIR 'Medication' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Medication' resource payload.
    """

    resource_type = "Medication"
    resource_subtype = "code_coding"
    transformer = MedicationCodeCodingTransformer
    expected_table_name = "medication_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
