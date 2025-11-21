"""
Test helper class for FHIR resource type Appointment subtype Specialty
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_specialty import (
    AppointmentSpecialtyTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "specialty_coding_system": "http://snomed.info/sct",
        "specialty_coding_code": "394814009",
        "specialty_coding_display": "General practice",
        "specialty_text": None,
        "id": "db4d85b2-f37a-41db-8164-ec9131c044e8",
        "appointment_id": "example",
    },
]


class AppointmentSpecialtyTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Appointment' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Appointment' resource.

    It predefines the resource type as 'Appointment'
    and initializes the resource with the specific 'Appointment' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Appointment'.

        resource (dict): The raw FHIR 'Appointment' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Appointment' resource payload.
    """

    resource_type = "Appointment"
    resource_subtype = "specialty"
    transformer = AppointmentSpecialtyTransformer
    expected_table_name = "appointment_specialty"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
