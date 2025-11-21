"""
Test helper class for FHIR resource type CarePlan subtype SupportingInfo
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanSupportingInfoTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "supporting_info_reference": "#support",
        "supporting_info_display": "support",
        "supporting_info_type": None,
        "id": "05fc597f-1b88-4ec8-8269-3c103acd9b07",
        "care_plan_id": "preg",
    },
]


class CarePlanSupportingInfoTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'CarePlan' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'CarePlan' resource.

    It predefines the resource type as 'CarePlan'
    and initializes the resource with the specific 'CarePlan' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'CarePlan'.

        resource (dict): The raw FHIR 'CarePlan' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'CarePlan' resource payload.
    """

    resource_type = "CarePlan"
    resource_subtype = "supporting_info"
    transformer = CarePlanSupportingInfoTransformer
    expected_table_name = "care_plan_supporting_info"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
