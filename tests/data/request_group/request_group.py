"""
Test helper class for FHIR resource type RequestGroup
"""

from radiant_fhir_transform_cli.transform.classes.request_group import (
    RequestGroupTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .request_group_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "kdn5-example",
        "resource_type": "RequestGroup",
        "group_identifier_type_text": None,
        "group_identifier_system": "http://example.org/treatment-group",
        "group_identifier_value": "00001",
        "group_identifier_period_start": None,
        "group_identifier_period_end": None,
        "status": "draft",
        "intent": "plan",
        "priority": "routine",
        "code_text": None,
        "subject_reference": "Patient/example",
        "subject_type": None,
        "subject_display": None,
        "encounter_reference": "Encounter/example",
        "encounter_type": None,
        "encounter_display": None,
        "authored_on": "2017-03-06T17:31:00Z",
        "author_reference": "Practitioner/1",
        "author_type": None,
        "author_display": None,
    },
]


class RequestGroupTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'RequestGroup' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'RequestGroup' resource.

    It predefines the resource type as 'RequestGroup'
    and initializes the resource with the specific 'RequestGroup' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'RequestGroup'.
        resource (dict): The raw FHIR 'RequestGroup' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'RequestGroup' resource payload.
    """

    resource_type = "RequestGroup"
    resource_subtype = None
    transformer = RequestGroupTransformer
    expected_table_name = "request_group"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
