"""
Test helper class for FHIR resource type MedicationRequest subtype CourseOfTherapyType Coding
"""

from radiant_fhir_transform_cli.transform.classes.medication_request import (
    MedicationRequestCourseOfTherapyTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .medication_request_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "course_of_therapy_type_coding_system": "http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy",
        "course_of_therapy_type_coding_code": "acute",
        "course_of_therapy_type_coding_display": "Short course (acute) therapy",
        "id": "2fcaa376-131c-43ab-83e5-6a00e60bcebf",
        "medication_request_id": "medrx0301",
    },
]


class MedicationRequestCourseOfTherapyTypeCodingTestHelper(
    FhirResourceTestHelper
):
    """
    A helper class for testing transformations of the FHIR 'MedicationRequest' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'MedicationRequest' resource.

    It predefines the resource type as 'MedicationRequest'
    and initializes the resource with the specific 'MedicationRequest' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'MedicationRequest'.

        resource (dict): The raw FHIR 'MedicationRequest' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'MedicationRequest' resource payload.
    """

    resource_type = "MedicationRequest"
    resource_subtype = "course_of_therapy_type_coding"
    transformer = MedicationRequestCourseOfTherapyTypeCodingTransformer
    expected_table_name = "medication_request_course_of_therapy_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
