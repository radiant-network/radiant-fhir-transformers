"""
Test helper class for FHIR resource type Coverage
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoverageTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "9876B1",
        "resource_type": "Coverage",
        "status": "active",
        "type_text": None,
        "policy_holder_reference": "Organization/CBI35",
        "policy_holder_type": None,
        "policy_holder_display": None,
        "subscriber_reference": "Patient/4",
        "subscriber_type": None,
        "subscriber_display": None,
        "subscriber_id": "CHOP12345678",
        "beneficiary_reference": "Patient/4",
        "beneficiary_type": None,
        "beneficiary_display": None,
        "dependent": "0",
        "relationship_text": None,
        "period_start": "2011-05-23",
        "period_end": "2012-05-23",
        "order": 2,
        "network": "5",
        "subrogation": True,
    },
]


class CoverageTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = CoverageTransformer
    expected_table_name = "coverage"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
