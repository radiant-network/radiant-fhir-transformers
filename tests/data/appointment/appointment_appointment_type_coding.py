"""
Test helper class for FHIR resource type Appointment subtype Appointment Type Coding
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_appointment_type_coding import (
    AppointmentAppointmentTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "appointment_type_coding_system": "http://terminology.hl7.org/CodeSystem/v2-0276",
        "appointment_type_coding_code": "FOLLOWUP",
        "appointment_type_coding_display": "A follow up visit from a previous appointment",
        "id": "0a357ee0-4d08-4ec5-aa8b-33572f3e91c1",
        "appointment_id": "example",
    },
]


class AppointmentAppointmentTypeCodingTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "appointment_type_coding"
    transformer = AppointmentAppointmentTypeCodingTransformer
    expected_table_name = "appointment_appointment_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
