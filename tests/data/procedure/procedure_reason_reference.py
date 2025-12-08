"""
Test helper class for FHIR resource type Procedure subtype ReasonReference
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureReasonReferenceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_reference_reference": "Condition/reason",
        "reason_reference_type": "Condition",
        "reason_reference_display": "The justification that the procedure was performed",
        "id": "e92077f3-dfc6-4cf8-a512-cb48874a7d67",
        "procedure_id": "f201",
    },
]


class ProcedureReasonReferenceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_reference"
    transformer = ProcedureReasonReferenceTransformer
    expected_table_name = "procedure_reason_reference"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
