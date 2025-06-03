"""
Test helper class for FHIR resource type Provenance subtype Target
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceTargetTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "provenance_id": "provenance",
        "target_reference": "target",
        "target_type": None,
        "target_display": None,
    }
]


class ProvenanceTargetTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "target"
    transformer = ProvenanceTargetTransformer
    expected_table_name = "provenance_target"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
