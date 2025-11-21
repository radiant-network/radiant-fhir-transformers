"""
Test helper class for FHIR resource type RelatedPerson subtype Name
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonNameTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "name_given": "Bénédicte",
        "name_use": None,
        "name_text": None,
        "name_family": "du Marché",
        "name_prefix": None,
        "name_suffix": None,
        "name_period_start": None,
        "name_period_end": None,
        "id": "f936100a-cf11-48fb-bdf1-7158cdc2d0f0",
        "related_person_id": "benedicte",
    },
]


class RelatedPersonNameTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "name"
    transformer = RelatedPersonNameTransformer
    expected_table_name = "related_person_name"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
