"""
Test helper class for FHIR resource type CarePlan subtype basedOn
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanBasedOnTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "based_on_reference": None,
        "based_on_display": "Management of Type 2 Diabetes",
        "based_on_type": None,
        "id": "eadfc3b5-e0fa-4090-aa8e-78883b4ecd99",
        "care_plan_id": "preg",
    },
]


class CarePlanBasedOnTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "based_on"
    transformer = CarePlanBasedOnTransformer
    expected_table_name = "care_plan_based_on"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
