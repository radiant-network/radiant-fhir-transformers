"""
Test helper class for FHIR resource type Procedure subtype UsedReference
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureUsedReferenceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "used_reference_reference": None,
        "used_reference_type": None,
        "used_reference_display": "Colonoscope device",
        "id": "b8815934-f571-4a7a-83c8-e23a571933c6",
        "procedure_id": "f201",
    },
]


class ProcedureUsedReferenceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "used_reference"
    transformer = ProcedureUsedReferenceTransformer
    expected_table_name = "procedure_used_reference"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
