"""
Test helper class for FHIR resource type RelatedPerson subtype Photo
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonPhotoTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "photo_content_type": "image/jpeg",
        "photo_language": None,
        "photo_url": "Binary/f016",
        "photo_size": None,
        "photo_title": None,
        "photo_creation": None,
        "id": "fa601a49-8972-46bf-82d1-895996a4b8d5",
        "related_person_id": "benedicte",
    },
]


class RelatedPersonPhotoTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'RelatedPerson' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'RelatedPerson' resource.

    It predefines the resource type as 'RelatedPerson'
    and initializes the resource with the specific 'RelatedPerson' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'RelatedPerson'.
        resource (dict): The raw FHIR 'RelatedPerson' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'RelatedPerson' resource payload.
    """

    resource_type = "RelatedPerson"
    resource_subtype = "photo"
    transformer = RelatedPersonPhotoTransformer
    expected_table_name = "related_person_photo"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
