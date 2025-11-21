"""
Test helper class for FHIR resource type RequestGroup subtype ReasonCode
"""

from radiant_fhir_transform_cli.transform.classes.request_group import (
    RequestGroupReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .request_group_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_code_coding": {
            "system": "http://snomed.info/sct",
            "code": "363443007",
            "display": "Malignant neoplasm of ovary (disorder)",
        },
        "reason_code_text": None,
        "id": "29679ea4-4c81-4751-9669-868d88a26cc4",
        "request_group_id": "kdn5-example",
    },
]


class RequestGroupReasonCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_code"
    transformer = RequestGroupReasonCodeTransformer
    expected_table_name = "request_group_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
