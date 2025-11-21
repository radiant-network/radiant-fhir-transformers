"""
Test helper class for FHIR resource type BodyStructure subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.body_structure import (
    BodyStructureIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .body_structure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_type_text": None,
        "identifier_system": "http://goodhealth.org/bodystructure/identifiers",
        "identifier_value": "12345",
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "13cc0c6c-a660-468b-a2de-4ed8a8cf6484",
        "body_structure_id": "tumor",
    },
]


class BodyStructureIdentifierTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'BodyStructure' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'BodyStructure' resource.

    It predefines the resource type as 'BodyStructure'
    and initializes the resource with the specific 'BodyStructure' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'BodyStructure'.
        resource (dict): The raw FHIR 'BodyStructure' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'BodyStructure' resource payload.
    """

    resource_type = "BodyStructure"
    resource_subtype = "identifier"
    transformer = BodyStructureIdentifierTransformer
    expected_table_name = "body_structure_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
