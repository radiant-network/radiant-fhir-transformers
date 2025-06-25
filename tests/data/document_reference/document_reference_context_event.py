"""
Test helper class for FHIR resource type DocumentReference subtype Context Event
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceContextEventTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "context_event_coding": [
            {
                "system": "http://ihe.net/xds/connectathon/eventCodes",
                "code": "T-D8200",
                "display": "Arm",
            }
        ],
        "context_event_text": None,
    },
]


class DocumentReferenceContextEventTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'DocumentReference' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'DocumentReference' resource.

    It predefines the resource type as 'DocumentReference'
    and initializes the resource with the specific 'DocumentReference' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'DocumentReference'.
        resource (dict): The raw FHIR 'DocumentReference' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'DocumentReference' resource payload.
    """

    resource_type = "DocumentReference"
    resource_subtype = "context_event"
    transformer = DocumentReferenceContextEventTransformer
    expected_table_name = "document_reference_context_event"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
