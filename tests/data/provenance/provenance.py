"""
Test helper class for FHIR resource type Provenance
"""

from radiant_fhir_transform_cli.transform.classes.provenance import (
    ProvenanceTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .provenance_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "provenance",
        "resource_type": "Provenance",
        "occurred_period_start": "2015-06-27",
        "occurred_period_end": "2015-06-28",
        "occurred_date_time": None,
        "recorded": "2015-06-27T08:39:24+10:00",
        "location_reference": "Location/location",
        "location_type": None,
        "location_display": None,
        "activity_text": None,
    },
]


class ProvenanceTestHelper(FhirResourceTestHelper):
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
    resource_subtype = None
    transformer = ProvenanceTransformer
    expected_table_name = "provenance"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
