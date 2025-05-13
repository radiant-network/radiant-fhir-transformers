"""
Test helper class for FHIR resource type Specimen subtype processing
"""

from radiant_fhir_transform_cli.transform.classes import (
    SpecimenProcessingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .specimen import RESOURCE

EXPECTED_OUTPUT = [
    {
        "specimen_id": "101",
        "processing_description":"Acidify to pH < 3.0 with 6 N HCl.",
        "processing_procedure_coding":[{"system": "http://terminology.hl7.org/CodeSystem/v2-0373","code": "ACID" }],
        "processing_procedure_text":None,
        "processing_additive":[{"display": "6 N HCl"}],
        "processing_time_date_time":"2015-08-18T08:10:00Z",
        "processing_time_period_start": None,
        "processing_time_period_end":None,
    },
]


class SpecimenProcessingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "processing"
    transformer = SpecimenProcessingTransformer
    expected_table_name = "specimen_processing"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
