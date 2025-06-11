"""
Test helper class for FHIR resource type RelatedPerson subtype Address
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonAddressTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "related_person_id": "benedicte",
        "address_use": None,
        "address_type": None,
        "address_text": None,
        "address_line": ["43, Place du Marché Sainte Catherine"],
        "address_city": "Paris",
        "address_district": None,
        "address_state": None,
        "address_postal_code": "75004",
        "address_country": "FRA",
        "address_period_start": None,
        "address_period_end": None,
    },
]


class RelatedPersonAddressTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "address"
    transformer = RelatedPersonAddressTransformer
    expected_table_name = "related_person_address"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
