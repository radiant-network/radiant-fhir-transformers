"""
Test helper class for FHIR resource type DocumentReference subtype SecurityLabel
"""

from radiant_fhir_transform_cli.transform.classes.document_reference import (
    DocumentReferenceSecurityLabelTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .document_reference_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "document_reference_id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
        "security_label_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality",
                "code": "N",
                "display": "normal",
            }
        ],
        "security_label_text": None,
    },
]


class DocumentReferenceSecurityLabelTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "security_label"
    transformer = DocumentReferenceSecurityLabelTransformer
    expected_table_name = "document_reference_security_label"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
