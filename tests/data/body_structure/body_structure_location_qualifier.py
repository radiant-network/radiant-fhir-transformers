"""
Test helper class for FHIR resource type BodyStructure subtype LocationQualifier
"""

from radiant_fhir_transform_cli.transform.classes.body_structure import (
    BodyStructureLocationQualifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .body_structure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "body_structure_id": "tumor",
        "location_qualifier_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "419161000",
                "display": "Unilateral left",
            }
        ],
        "location_qualifier_text": "Left",
    },
    {
        "body_structure_id": "tumor",
        "location_qualifier_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "263929005",
                "display": "Volar",
            }
        ],
        "location_qualifier_text": "Volar",
    },
]


class BodyStructureLocationQualifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "location_qualifier"
    transformer = BodyStructureLocationQualifierTransformer
    expected_table_name = "body_structure_location_qualifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
