"""
Test helper class for FHIR resource type RelatedPerson subtype Communication
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonCommunicationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "related_person_id": "benedicte",
        "communication_language_coding": [
            {
                "system": "urn:ietf:bcp:47",
                "code": "en-US",
                "display": "English (United States)",
            }
        ],
        "communication_language_text": "American English",
        "communication_preferred": True,
    },
]


class RelatedPersonCommunicationTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "communication"
    transformer = RelatedPersonCommunicationTransformer
    expected_table_name = "related_person_communication"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
