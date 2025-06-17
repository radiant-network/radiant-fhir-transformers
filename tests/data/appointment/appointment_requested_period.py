"""
Test helper class for FHIR resource type Appointment subtype Requested Period
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_requested_period import (
    AppointmentRequestedPeriodTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "appointment_id": "example",
        "requested_period_start": "2016-06-02",
        "requested_period_end": "2016-06-09",
    }
]


class AppointmentRequestedPeriodTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "requested_period"
    transformer = AppointmentRequestedPeriodTransformer
    expected_table_name = "appointment_requested_period"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
