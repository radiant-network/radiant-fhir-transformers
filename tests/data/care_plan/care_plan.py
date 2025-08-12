"""
Test helper class for FHIR resource type CarePlan
"""

from radiant_fhir_transform_cli.transform.classes.care_plan.care_plan import (
    CarePlanTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "preg",
        "resource_type": "CarePlan",
        "status": "active",
        "intent": "plan",
        "title": None,
        "description": None,
        "subject_reference": "1",
        "subject_display": "Eve Everywoman",
        "subject_reference_type": "Patient",
        "encounter_reference": None,
        "encounter_display": None,
        # "encounter_reference_type": None,
        "period_start": "2013-01-01",
        "period_end": "2013-10-01",
        "created": None,
        "author_reference": None,
        "author_display": None,
        # "author_reference_type": None,
    },
]


class CarePlanTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = CarePlanTransformer
    expected_table_name = "care_plan"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
