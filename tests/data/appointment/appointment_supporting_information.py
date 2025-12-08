"""
Test helper class for FHIR resource type Appointment subtype Supporting Information
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_supporting_information import (
    AppointmentSupportingInformationTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "supporting_information_reference": "DiagnosticReport/ultrasound",
        "supporting_information_type": None,
        "supporting_information_display": None,
        "id": "90a076b5-50b8-4279-8ebf-8117fb9eeced",
        "appointment_id": "example",
    },
]


class AppointmentSupportingInformationTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "supporting_information"
    transformer = AppointmentSupportingInformationTransformer
    expected_table_name = "appointment_supporting_information"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
