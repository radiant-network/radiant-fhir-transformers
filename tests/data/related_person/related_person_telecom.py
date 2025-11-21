"""
Test helper class for FHIR resource type RelatedPerson subtype Telecom
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonTelecomTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "telecom_system": "phone",
        "telecom_value": "+33 (237) 998327",
        "telecom_use": None,
        "telecom_rank": None,
        "telecom_period_start": None,
        "telecom_period_end": None,
        "id": "1d5ae2ce-8662-44c4-a507-a2c3860e9f24",
        "related_person_id": "benedicte",
    },
]


class RelatedPersonTelecomTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "telecom"
    transformer = RelatedPersonTelecomTransformer
    expected_table_name = "related_person_telecom"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
