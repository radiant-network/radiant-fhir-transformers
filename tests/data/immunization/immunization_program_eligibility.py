"""
Test helper class for FHIR resource type Immunization subtype ProgramEligibility
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationProgramEligibilityTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "program_eligibility_coding_system": "http://terminology.hl7.org/CodeSystem/immunization-program-eligibility",
        "program_eligibility_coding_code": "ineligible",
        "program_eligibility_text": None,
        "id": "195a9976-246a-4f6c-a57e-65a1bce39145",
        "immunization_id": "example",
    },
]


class ImmunizationProgramEligibilityTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "program_eligibility"
    transformer = ImmunizationProgramEligibilityTransformer
    expected_table_name = "immunization_program_eligibility"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
