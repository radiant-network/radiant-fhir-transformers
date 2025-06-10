"""
Test helper class for FHIR resource type CarePlan subtype InstantiatesCanonical
"""

from radiant_fhir_transform_cli.transform.classes.care_plan import (
    CarePlanInstantiatesCanonicalTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "care_plan_id": "preg",
        "instantiates_canonical": "http://example.org/fhir/CarePlanDefinition/KDN5",
    }
]


class CarePlanInstantiatesCanonicalTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "instantiates_canonical"
    transformer = CarePlanInstantiatesCanonicalTransformer
    expected_table_name = "care_plan_instantiates_canonical"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
