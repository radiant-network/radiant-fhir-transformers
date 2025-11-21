"""
Test helper class for FHIR resource type Procedure subtype Category Coding
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureCategoryCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "category_coding_system": "http://snomed.info/sct",
        "category_coding_code": "103693007",
        "category_coding_display": "Diagnostic procedure",
        "id": "ee8d5408-99ba-46bd-9589-e2c1e45c4a9f",
        "procedure_id": "f201",
    },
]


class ProcedureCategoryCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Procedure' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Procedure' resource.

    It predefines the resource type as 'Procedure'
    and initializes the resource with the specific 'Procedure' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Procedure'.

        resource (dict): The raw FHIR 'Procedure' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Procedure' resource payload.
    """

    resource_type = "Procedure"
    resource_subtype = "category_coding"
    transformer = ProcedureCategoryCodingTransformer
    expected_table_name = "procedure_category_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
