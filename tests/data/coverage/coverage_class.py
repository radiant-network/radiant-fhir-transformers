"""
Test helper class for FHIR resource type Coverage subtype Class
"""

from radiant_fhir_transform_cli.transform.classes.coverage import (
    CoverageClassTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .coverage_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "coverage_id": "9876B1",
        "class_type_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
                "code": "group",
            }
        ],
        "class_type_text": None,
        "class_value": "CB135",
        "class_name": "Corporate Baker's Inc. Local #35",
    },
    {
        "coverage_id": "9876B1",
        "class_type_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
                "code": "subgroup",
            }
        ],
        "class_type_text": None,
        "class_value": "123",
        "class_name": "Trainee Part-time Benefits",
    },
    {
        "coverage_id": "9876B1",
        "class_type_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
                "code": "plan",
            }
        ],
        "class_type_text": None,
        "class_value": "B37FC",
        "class_name": "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC",
    },
]


class CoverageClassTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Coverage' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Coverage' resource.

    It predefines the resource type as 'Coverage'
    and initializes the resource with the specific 'Coverage' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Coverage'.
        resource (dict): The raw FHIR 'Coverage' resource payload to be tested.
        expected_output (dict): The expected transformation result of the
          'Coverage' resource payload.
    """

    resource_type = "Coverage"
    resource_subtype = "class"
    transformer = CoverageClassTransformer
    expected_table_name = "coverage_class"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
