"""
Test helper class for FHIR resource type Immunization subtype VaccineCode Coding
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationVaccineCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "immunization_id": "example",
        "vaccine_code_coding_system": "urn:oid:1.2.36.1.2001.1005.17",
        "vaccine_code_coding_code": "FLUVAX",
        "vaccine_code_coding_display": None,
    },
]


class ImmunizationVaccineCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "vaccine_code_coding"
    transformer = ImmunizationVaccineCodeCodingTransformer
    expected_table_name = "immunization_vaccine_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
