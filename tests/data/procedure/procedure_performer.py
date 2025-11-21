"""
Test helper class for FHIR resource type Procedure subtype Performer
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedurePerformerTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "performer_function_coding_system": "http://snomed.info/sct",
        "performer_function_coding_code": "310512001",
        "performer_function_coding_display": "Medical oncologist",
        "performer_function_text": None,
        "performer_actor_reference": "Practitioner/f201",
        "performer_actor_type": None,
        "performer_actor_display": "Dokter Bronsig",
        "performer_on_behalf_of_reference": None,
        "performer_on_behalf_of_type": None,
        "performer_on_behalf_of_display": None,
        "id": "d8e4e3b3-9884-48fd-9dfb-aecbce90b261",
        "procedure_id": "f201",
    },
]


class ProcedurePerformerTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "performer"
    transformer = ProcedurePerformerTransformer
    expected_table_name = "procedure_performer"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
