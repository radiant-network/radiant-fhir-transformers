"""
Test helper class for FHIR resource type BodyStructure
"""

from radiant_fhir_transform_cli.transform.classes.body_structure import (
    BodyStructureTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .body_structure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "tumor",
        "resource_type": "BodyStructure",
        "active": True,
        "morphology_text": "Splenic mass",
        "location_text": "Spleen",
        "description": "7 cm maximum diameter",
        "patient_reference": "example",
        "patient_type": None,
        "patient_display": None,
    }
]


class BodyStructureTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = BodyStructureTransformer
    expected_table_name = "body_structure"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
