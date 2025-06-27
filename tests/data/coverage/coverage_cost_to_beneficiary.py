"""
Test helper class for FHIR resource type Coverage subtype CostToBeneficiary
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoverageCostToBeneficiaryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "coverage_id": "9876B1",
        "cost_to_beneficiary_type_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/coverage-copay-type",
                "code": "gpvisit",
            }
        ],
        "cost_to_beneficiary_type_text": None,
        "cost_to_beneficiary_value_quantity_value": None,
        "cost_to_beneficiary_value_quantity_unit": None,
        "cost_to_beneficiary_value_quantity_system": None,
        "cost_to_beneficiary_value_quantity_code": None,
        "cost_to_beneficiary_value_money_value": "20.0",
        "cost_to_beneficiary_value_money_currency": "USD",
        "cost_to_beneficiary_exception": [
            {
                "type": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception",
                            "code": "retired",
                        }
                    ]
                },
                "period": {
                    "start": "2018-01-01",
                    "end": "2018-12-31",
                },
            }
        ],
    },
]


class CoverageCostToBeneficiaryTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "cost_to_beneficiary"
    transformer = CoverageCostToBeneficiaryTransformer
    expected_table_name = "coverage_cost_to_beneficiary"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
