"""
Test helper class for FHIR resource type MedicationRequest subtype Category
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "category_text": "Requests for medications in inpatient or acute care settings",
        "id": "e222f750-97de-47ee-a598-10d62858f1f6",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestCategoryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "category"
    transformer = MedicationRequestCategoryTransformer
    expected_table_name = "medication_request_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
