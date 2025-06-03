"""
Test helper class for FHIR resource type Provenance subtype Reason
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceReasonTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provenance_id": "provenance",
        "reason_coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "3457005",
                "display": "Referral",
            }
        ],
        "reason_text": None,
    }
]


class ProvenanceReasonTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason"
    transformer = ProvenanceReasonTransformer
    expected_table_name = "provenance_reason"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
