"""
Test helper class for FHIR resource type RelatedPerson
"""

from radiant_fhir_transform_cli.transform.classes.related_person import (
    RelatedPersonTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .related_person_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "benedicte",
        "resource_type": "RelatedPerson",
        "active": True,
        "patient_reference": "example",
        "patient_type": None,
        "patient_display": None,
        "gender": "female",
        "birth_date": "2012-03-11",
        "period_start": "2012-03-11",
        "period_end": None,
    }
]


class RelatedPersonTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = RelatedPersonTransformer
    expected_table_name = "related_person"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
