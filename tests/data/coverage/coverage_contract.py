"""
Test helper class for FHIR resource type Coverage subtype Contract
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoverageContractTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "contract_reference": "Contract/INS-101",
        "contract_type": None,
        "contract_display": None,
        "id": "963f460b-bb76-4a47-bd14-8bf2db08ca3a",
        "coverage_id": "9876B1",
    },
]


class CoverageContractTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "contract"
    transformer = CoverageContractTransformer
    expected_table_name = "coverage_contract"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
