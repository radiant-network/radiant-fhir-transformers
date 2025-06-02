"""
Test helper class for FHIR resource type Provenance subtype Signature
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceSignatureTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provenance_id": "provenance",
        "signature_type": [
            {
                "system": "urn:iso-astm:E1762-95:2013",
                "code": "1.2.840.10065.1.12.1.5",
                "display": "Verification Signature",
            }
        ],
        "signature_when": "2015-08-27T08:39:24+10:00",
        "signature_who_reference": "Practitioner/signature",
        "signature_who_type": None,
        "signature_who_display": None,
        "signature_on_behalf_of_reference": None,
        "signature_on_behalf_of_type": None,
        "signature_on_behalf_of_display": None,
        "signature_target_format": "application/fhir+xml",
        "signature_sig_format": "application/signature+xml",
    },
]


class ProvenanceSignatureTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Provenance' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Provenance' resource.

    It predefines the resource type as 'Provenance'
    and initializes the resource with the specific 'Provenance' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Provenance'.

        resource (dict): The raw FHIR 'Provenance' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Provenance' resource payload.
    """

    resource_type = "Provenance"
    resource_subtype = "signature"
    transformer = ProvenanceSignatureTransformer
    expected_table_name = "provenance_signature"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
