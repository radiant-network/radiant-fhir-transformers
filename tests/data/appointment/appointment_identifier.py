"""
Test helper class for FHIR resource type Appointment subtype Identifier 
"""

from radiant_fhir_transform_cli.transform.classes.appointment.appointment_identifier import (
    AppointmentIdentifierTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "identifier_use": None,
        "identifier_system": "http://example.org/sampleappointment-identifier",
        "identifier_value": "123",
        "identifier_type_text": None,
        "identifier_period_start": None,
        "identifier_period_end": None,
        "id": "08554ea5-1c2d-4c39-8245-964ed0b2cd22",
        "appointment_id": "example",
    },
]


class AppointmentIdentifierTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "identifier"
    transformer = AppointmentIdentifierTransformer
    expected_table_name = "appointment_identifier"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
