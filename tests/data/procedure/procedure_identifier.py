"""
Test helper class for FHIR resource type Procedure subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.procedure import (
    ProcedureIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .procedure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "procedure_id": "f201",
        "identifier_use": "usual",
        "identifier_type_text": "ORD",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.861.1.7.2.798268",
        "identifier_value": "3287774",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
    {
        "procedure_id": "f201",
        "identifier_use": "usual",
        "identifier_type_text": "EAP",
        "identifier_system": "urn:oid:1.2.840.114350.1.13.861.1.7.2.696580",
        "identifier_value": "307",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class ProcedureIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = ProcedureIdentifierTransformer
    expected_table_name = "procedure_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
