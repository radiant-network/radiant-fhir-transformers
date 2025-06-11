"""
Test helper class for FHIR resource type BodyStructure subtype Morphology Coding
"""

from radiant_fhir_transform_cli.transform.classes.body_structure import (
    BodyStructureMorphologyCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .body_structure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "body_structure_id": "tumor",
        "morphology_coding_system": "http://snomed.info/sct",
        "morphology_coding_code": "4147007",
        "morphology_coding_display": "Mass (morphologic abnormality)",
    },
]


class BodyStructureMorphologyCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "morphology_coding"
    transformer = BodyStructureMorphologyCodingTransformer
    expected_table_name = "body_structure_morphology_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
