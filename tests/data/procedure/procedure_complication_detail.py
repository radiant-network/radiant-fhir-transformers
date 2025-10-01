"""
Test helper class for FHIR resource type Procedure subtype ComplicationDetail
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureComplicationDetailTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "procedure_id": "f201",
        "complication_detail_reference": "complication",
        "complication_detail_reference_type": "Condition",
        "complication_detail_display": None,
    }
]


class ProcedureComplicationDetailTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "complication_detail"
    transformer = ProcedureComplicationDetailTransformer
    expected_table_name = "procedure_complication_detail"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
