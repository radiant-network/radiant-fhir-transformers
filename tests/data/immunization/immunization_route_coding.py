"""
Test helper class for FHIR resource type Immunization subtype Route Coding
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationRouteCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "immunization_id": "example",
        "route_coding_system": "http://terminology.hl7.org/CodeSystem/v3-RouteOfAdministration",
        "route_coding_code": "IM",
        "route_coding_display": "Injection, intramuscular",
    },
]


class ImmunizationRouteCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Immunization' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Immunization' resource.

    It predefines the resource type as 'Immunization'
    and initializes the resource with the specific 'Immunization' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Immunization'.
        resource (dict): The raw FHIR 'Immunization' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Immunization' resource payload.
    """

    resource_type = "Immunization"
    resource_subtype = "route_coding"
    transformer = ImmunizationRouteCodingTransformer
    expected_table_name = "immunization_route_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
