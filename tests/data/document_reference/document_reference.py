"""
Test helper class for FHIR resource type DocumentReference
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "resource_type": "DocumentReference",
        "status": "current",
        "doc_status": "preliminary",
        "subject_reference": "eiCbDCEzFk6wR6UNlcWziySVQrlN47NTRvxPwgT4P3883",
        "subject_display": "JEK, Danger",
        "date": "2021-10-27T19:02:27Z",
        "custodian_display": None,
        "description": None,
    }
]


class DocumentReferenceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = DocumentReferenceTransformer
    expected_table_name = "document_reference"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
