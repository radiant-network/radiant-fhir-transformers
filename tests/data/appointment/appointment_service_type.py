"""
Test helper class for FHIR resource type Appointment subtype Service Type
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_service_type import (
    AppointmentServiceTypeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "service_type_coding_code": "52",
        "service_type_coding_display": "General Discussion",
        "service_type_text": None,
        "id": "d0d7acdd-dd94-448e-b916-2542ea0f5fd9",
        "appointment_id": "example",
    },
]


class AppointmentServiceTypeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "service_type"
    transformer = AppointmentServiceTypeTransformer
    expected_table_name = "appointment_service_type"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
