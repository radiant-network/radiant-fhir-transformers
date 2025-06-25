"""
Test helper class for FHIR resource type DocumentReference subtype Type Coding
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "type_coding_system": "urn:oid:1.2.840.114350.1.13.5325.1.7.4.737880.5010",
        "type_coding_code": "1",
        "type_coding_display": "Progress Notes",
    },
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "type_coding_system": "urn:oid:1.2.840.114350.1.72.727879.69848980",
        "type_coding_code": "1",
        "type_coding_display": "Progress Notes",
    },
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "type_coding_system": "http://loinc.org",
        "type_coding_code": "11506-3",
        "type_coding_display": "Progress note",
    },
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "type_coding_system": "http://loinc.org",
        "type_coding_code": "75492-9",
        "type_coding_display": "Risk assessment and screening note",
    },
]


class DocumentReferenceTypeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "type_coding"
    transformer = DocumentReferenceTypeCodingTransformer
    expected_table_name = "document_reference_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
