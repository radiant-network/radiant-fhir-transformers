"""
Test helper class for FHIR resource type Procedure subtype DataAbsentReason
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureDataAbsentReasonTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "value_code": "not-applicable",
        "id": "3a62cbdb-df70-4663-a3a2-02692652efc5",
        "procedure_id": "f201",
    },
]


class ProcedureDataAbsentReasonTestHelper(FhirResourceTestHelper):
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
    resource_component = "data_absent_reason"
    transformer = ProcedureDataAbsentReasonTransformer
    expected_table_name = "procedure_data_absent_reason"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
