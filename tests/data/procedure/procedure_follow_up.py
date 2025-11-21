"""
Test helper class for FHIR resource type Procedure subtype FollowUp
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureFollowUpTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "follow_up_coding_system": "http://snomed.info/sct",
        "follow_up_coding_code": "183651009",
        "follow_up_coding_display": "Chemotherapy follow-up (procedure)",
        "follow_up_text": None,
        "id": "6f591259-a534-4b3f-b539-424dd41d0bb5",
        "procedure_id": "f201",
    },
]


class ProcedureFollowUpTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "follow_up"
    transformer = ProcedureFollowUpTransformer
    expected_table_name = "procedure_follow_up"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
