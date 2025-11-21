"""
Test helper class for FHIR resource type Coverage subtype Relationship Coding
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoverageRelationshipCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "relationship_coding_system": None,
        "relationship_coding_code": "self",
        "relationship_coding_display": None,
        "id": "b23698de-f032-4ac0-a9c0-0e2228dfb80a",
        "coverage_id": "9876B1",
    },
]


class CoverageRelationshipCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "relationship_coding"
    transformer = CoverageRelationshipCodingTransformer
    expected_table_name = "coverage_relationship_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
