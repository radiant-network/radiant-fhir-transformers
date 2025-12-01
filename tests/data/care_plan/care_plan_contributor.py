"""
Test helper class for FHIR resource type CarePlan subtype contributor
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanContributorTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "care_plan_id": "preg",
        "id": "51d90d7c-e50f-4618-9d1d-d07aa9cd8bda",
        "contributor_reference": "Practitioner/example",
        "contributor_display": "Peter Example",
        "contributor_type": None,
    },
]


class CarePlanContributorTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "contributor"
    transformer = CarePlanContributorTransformer
    expected_table_name = "care_plan_contributor"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
