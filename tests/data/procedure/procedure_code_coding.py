"""
Test helper class for FHIR resource type Procedure subtype Code Coding
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureCodeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "code_coding_system": "http://snomed.info/sct",
        "code_coding_code": "367336001",
        "code_coding_display": "Chemotherapy",
        "id": "87fbc387-e1b1-4cfc-8d30-06627593d52f",
        "procedure_id": "f201",
    },
]


class ProcedureCodeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "code_coding"
    transformer = ProcedureCodeCodingTransformer
    expected_table_name = "procedure_code_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
