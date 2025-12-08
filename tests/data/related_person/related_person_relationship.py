"""
Test helper class for FHIR resource type RelatedPerson subtype Relationship
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonRelationshipTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "relationship_coding": {
            "system": "http://terminology.hl7.org/CodeSystem/v2-0131",
            "code": "N",
        },
        "relationship_text": None,
        "id": "656bcce6-bf3f-4371-a5b9-dbd435045059",
        "related_person_id": "benedicte",
    },
    {
        "relationship_coding": {
            "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
            "code": "WIFE",
        },
        "relationship_text": None,
        "id": "7a7c5e10-92d9-4dd9-988f-4c8e54b765fd",
        "related_person_id": "benedicte",
    },
]


class RelatedPersonRelationshipTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "relationship"
    transformer = RelatedPersonRelationshipTransformer
    expected_table_name = "related_person_relationship"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
