"""
Test helper class for FHIR resource type Coverage subtype Payor
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoveragePayorTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "payor_reference": "Organization/2",
        "payor_type": None,
        "payor_display": None,
        "id": "1f0f6f5a-7c06-4c3f-8f86-5701a3072768",
        "coverage_id": "9876B1",
    },
]


class CoveragePayorTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Coverage' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Coverage' resource.

    It predefines the resource type as 'Coverage'
    and initializes the resource with the specific 'Coverage' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Coverage'.
        resource (dict): The raw FHIR 'Coverage' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Coverage' resource payload.
    """

    resource_type = "Coverage"
    resource_subtype = "payor"
    transformer = CoveragePayorTransformer
    expected_table_name = "coverage_payor"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
