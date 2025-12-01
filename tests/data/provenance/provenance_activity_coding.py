"""
Test helper class for FHIR resource type Provenance subtype Activity Coding
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceActivityCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "activity_coding_system": "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion",
        "activity_coding_code": "AU",
        "activity_coding_display": "authenticated",
        "id": "88e90e47-403f-44a3-b9e3-8b90b0c87d84",
        "provenance_id": "provenance",
    },
]


class ProvenanceActivityCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "activity_coding"
    transformer = ProvenanceActivityCodingTransformer
    expected_table_name = "provenance_activity_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
