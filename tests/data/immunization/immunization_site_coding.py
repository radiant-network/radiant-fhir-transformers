"""
Test helper class for FHIR resource type Immunization subtype Site Coding
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationSiteCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "site_coding_system": "http://terminology.hl7.org/CodeSystem/v3-ActSite",
        "site_coding_code": "LA",
        "site_coding_display": "left arm",
        "id": "95a7c381-2829-432c-ac0e-5477d5dd125d",
        "immunization_id": "example",
    },
]


class ImmunizationSiteCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "site_coding"
    transformer = ImmunizationSiteCodingTransformer
    expected_table_name = "immunization_site_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
