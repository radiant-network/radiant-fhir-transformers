"""
Test helper class for FHIR resource type List subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.list import (
    ListIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .list_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "list_id": "med-list",
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": "urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59",
        "identifier_value": "23974652",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class ListIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'List' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'List' resource.

    It predefines the resource type as 'List'
    and initializes the resource with the specific 'List' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'List'.
        resource (dict): The raw FHIR 'List' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'List' resource payload.
    """

    resource_type = "List"
    resource_subtype = "identifier"
    transformer = ListIdentifierTransformer
    expected_table_name = "list_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
