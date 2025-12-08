"""
Test helper class for FHIR resource type DocumentReference Content
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceContentTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "content_attachment_content_type": "application/hl7-v3+xml",
        "content_attachment_language": "en-US",
        "content_attachment_url": "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510",
        "content_attachment_size": 3654,
        "content_attachment_title": "Physical",
        "content_attachment_creation": "2004-12-23",
        "content_format_system": "urn:oid:1.3.6.1.4.1.19376.1.2.3",
        "content_format_code": "urn:ihe:pcc:handp:2008",
        "content_format_display": "History and Physical Specification",
        "id": "d8dbca12-b023-4735-9948-3d4de54f2fa4",
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
    },
]


class DocumentReferenceContentTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "content"
    transformer = DocumentReferenceContentTransformer
    expected_table_name = "document_reference_content"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
