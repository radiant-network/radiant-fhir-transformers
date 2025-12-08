"""
Test helper class for FHIR resource type Procedure subtype StatusReason Coding
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureStatusReasonCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "status_reason_coding_system": "http://snomed.info/sct",
        "status_reason_coding_code": "182992009",
        "status_reason_coding_display": "Treatment completed (situation)",
        "id": "40b5a39e-edc9-4758-8fb0-15f51974c823",
        "procedure_id": "f201",
    },
]


class ProcedureStatusReasonCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "status_reason_coding"
    transformer = ProcedureStatusReasonCodingTransformer
    expected_table_name = "procedure_status_reason_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
