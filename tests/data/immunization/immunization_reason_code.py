"""
Test helper class for FHIR resource type Immunization subtype ReasonCode
"""

from radiant_fhir_transform_cli.transform.classes.immunization import (
    ImmunizationReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .immunization_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_code_coding_system": "http://snomed.info/sct",
        "reason_code_coding_code": "429060002",
        "reason_code_text": None,
        "id": "6961dfe9-39a0-470c-af08-52f43aaf9cdb",
        "immunization_id": "example",
    },
]


class ImmunizationReasonCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_code"
    transformer = ImmunizationReasonCodeTransformer
    expected_table_name = "immunization_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
