"""
Test helper class for FHIR resource type Procedure subtype PartOf
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedurePartOfTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "part_of_reference": "Procedure/part-of-referenced-event",
        "part_of_type": None,
        "part_of_display": "Part of referenced event",
        "id": "25405367-bdc1-421b-a4a9-81e88420a0e5",
        "procedure_id": "f201",
    },
]


class ProcedurePartOfTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "part_of"
    transformer = ProcedurePartOfTransformer
    expected_table_name = "procedure_part_of"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
