"""
Test helper class for FHIR resource type Coverage subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoverageIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": "http://benefitsinc.com/certificate",
        "identifier_value": "12345",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "0f244e38-20ca-4f79-8e56-20760b5be12a",
        "coverage_id": "9876B1",
    },
]


class CoverageIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = CoverageIdentifierTransformer
    expected_table_name = "coverage_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
