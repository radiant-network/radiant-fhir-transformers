"""
Test helper class for FHIR resource type BodyStructure subtype Image
"""

from radiant_fhir_transform_cli.transform.classes.body_structure import (
    BodyStructureImageTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .body_structure_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "image_content_type": "application/dicom",
        "image_language": None,
        "image_url": "http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details",
        "image_size": None,
        "image_title": None,
        "image_creation": None,
        "id": "932827b8-8078-492d-8540-02d2981cda8d",
        "body_structure_id": "tumor",
    },
]


class BodyStructureImageTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "image"
    transformer = BodyStructureImageTransformer
    expected_table_name = "body_structure_image"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
