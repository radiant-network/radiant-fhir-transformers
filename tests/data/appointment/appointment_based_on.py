"""
Test helper class for FHIR resource type Appointment subtype Based On
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_based_on import (
    AppointmentBasedOnTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "based_on_reference": "ServiceRequest/myringotomy",
        "based_on_type": None,
        "based_on_display": None,
        "id": "a7f0d789-fd30-4101-a574-f5e4eb064eee",
        "appointment_id": "example",
    },
]


class AppointmentBasedOnTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "based_on"
    transformer = AppointmentBasedOnTransformer
    expected_table_name = "appointment_based_on"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
