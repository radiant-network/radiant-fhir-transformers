"""
Test helper class for FHIR resource type Observation subtype Category
"""

from radiant_fhir_transform_cli.transform.classes.observation import (
    ObservationCategoryTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .observation_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "category_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory",
                "display": "Laboratory",
            }
        ],
        "category_text": "Laboratory",
    },
    {
        "observation_id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
        "category_coding": [
            {
                "system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.798268.30",
                "code": "lab",
            }
        ],
        "category_text": "Lab",
    },
]


class ObservationCategoryTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Observation' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Observation' resource.

    It predefines the resource type as 'Observation'
    and initializes the resource with the specific 'Observation' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Observation'.
        resource (dict): The raw FHIR 'Observation' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Observation' resource payload.
    """

    resource_type = "Observation"
    resource_subtype = "category"
    transformer = ObservationCategoryTransformer
    expected_table_name = "observation_category"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
