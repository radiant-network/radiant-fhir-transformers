"""
Test helper class for FHIR resource type Condition subtype Verification Status Coding
"""

from radiant_fhir_transform_cli.transform.classes.condition.condition_verification_status_coding import (
    ConditionVerificationStatusCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .condition_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "verification_status_coding_system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
        "verification_status_coding_code": "confirmed",
        "verification_status_coding_display": None,
        "id": "4a104090-0daf-4f01-91a7-fa748bfec2c9",
        "condition_id": "f201",
    },
]


class ConditionVerificationStatusCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Condition' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Condition' resource.

    It predefines the resource type as 'Condition'
    and initializes the resource with the specific 'Condition' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Condition'.

        resource (dict): The raw FHIR 'Condition' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Condition' resource payload.
    """

    resource_type = "Condition"
    resource_subtype = "verification_status_coding"
    transformer = ConditionVerificationStatusCodingTransformer
    expected_table_name = "condition_verification_status_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
