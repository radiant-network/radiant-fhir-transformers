"""
Test helper class for FHIR resource type CarePlan subtype identifier
"""

from radiant_fhir_transform_cli.transform.classes import (
    CarePlanIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .care_plan import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_type_text": None,
        "identifier_system": "http://www.bmc.nl/zorgportal/identifiers/careplans",
        "identifier_value": "CP2903",
        "identifier_use": "official",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "7cb9e121-de10-4ca7-ba74-2c99bb2700cf",
        "care_plan_id": "preg",
    },
]


class CarePlanIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = CarePlanIdentifierTransformer
    expected_table_name = "care_plan_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
