"""
Test helper class for FHIR resource type RelatedPerson subtype Identifier
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "related_person_id": "benedicte",
        "identifier_use": "usual",
        "identifier_type_text": "INSEE",
        "identifier_system": "urn:oid:1.2.250.1.61",
        "identifier_value": "272117510400399",
        "identifier_period_start": None,
        "identifier_period_end": None,
    },
]


class RelatedPersonIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = RelatedPersonIdentifierTransformer
    expected_table_name = "related_person_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
