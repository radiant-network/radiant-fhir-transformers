"""
Test helper class for FHIR resource type Appointment subtype Reason Code
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_reason_code import (
    AppointmentReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "appointment_id": "example",
        "reason_code_coding": [
            {"system": "http://snomed.info/sct", "code": "413095006"}
        ],
        "reason_code_text": "Clinical Review",
    }
]


class AppointmentReasonCodeTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "reason_code"
    transformer = AppointmentReasonCodeTransformer
    expected_table_name = "appointment_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
