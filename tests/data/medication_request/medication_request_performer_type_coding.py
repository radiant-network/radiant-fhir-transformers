"""
Test helper class for FHIR resource type MedicationRequest subtype PerformerType Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestPerformerTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "performer_type_coding_system": "http://snomed.info/sct",
        "performer_type_coding_code": "26369006",
        "performer_type_coding_display": "Public Health Nurse",
        "id": "b833b2ba-6159-47d7-9692-e84e2ed476b8",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestPerformerTypeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "performer_type_coding"
    transformer = MedicationRequestPerformerTypeCodingTransformer
    expected_table_name = "medication_request_performer_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
