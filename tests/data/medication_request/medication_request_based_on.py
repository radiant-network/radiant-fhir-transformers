"""
Test helper class for FHIR resource type MedicationRequest subtype BasedOn
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestBasedOnTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "medication_request_id": "medrx0301",
        "based_on_reference": "fM4L7yx-lQwmJcrS7MAT3m1zkSuH8v8LVdM1dkvXzDPc4",
        "based_on_reference_type": "CarePlan",
        "based_on_display": "BMT Supportive Care Plan",
    },
    {
        "medication_request_id": "medrx0301",
        "based_on_reference": "ee02A2FZtICYRsDjH4.zr1tqyCMSVk0A6Uqb--g8q7eQ3",
        "based_on_reference_type": "MedicationRequest",
        "based_on_display": "acetaminophen susp 140.8 mg",
    },
]


class MedicationRequestBasedOnTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "based_on"
    transformer = MedicationRequestBasedOnTransformer
    expected_table_name = "medication_request_based_on"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
