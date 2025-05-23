"""
Test helper class for FHIR resource type Specimen subtype collectionBodySiteCoding
"""

from radiant_fhir_transform_cli.transform.classes import (
    SpecimenCollectionBodySiteCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen import RESOURCE

EXPECTED_OUTPUT = [
    {
        "specimen_id": "101",
        "collection_body_site_coding_system": "http://snomed.info/sct",
        "collection_body_site_coding_code": "49852007",
        "collection_body_site_coding_display": "Structure of median cubital vein (body structure)",
    },
]


class SpecimenCollectionBodySiteCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Specimen' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Specimen' resource.

    It predefines the resource type as 'Specimen'
    and initializes the resource with the specific 'Specimen' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Specimen'.

        resource (dict): The raw FHIR 'Specimen' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Specimen' resource payload.
    """

    resource_type = "Specimen"
    resource_subtype = "collection_body_site_coding"
    transformer = SpecimenCollectionBodySiteCodingTransformer
    expected_table_name = "specimen_collection_body_site_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
