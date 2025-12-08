"""
Test helper class for FHIR resource type Specimen subtype typeCoding
"""

from radiant_fhir_transform_cli.transform.classes import (
    SpecimenTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen import RESOURCE

EXPECTED_OUTPUT = [
    {
        "type_coding_system": "http://snomed.info/sct",
        "type_coding_code": "122555007",
        "type_coding_display": "Venous blood specimen",
        "id": "e6d72782-ee4b-4f93-a01c-037a10a22b69",
        "specimen_id": "101",
    },
]


class SpecimenTypeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "type_coding"
    transformer = SpecimenTypeCodingTransformer
    expected_table_name = "specimen_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
