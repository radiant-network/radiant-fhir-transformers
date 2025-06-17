"""
Test helper class for FHIR resource type Appointment
"""

from radiant_fhir_transform_cli.transform.classes.appointment import (
    AppointmentTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .appointment_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "id": "example",
        "resource_type": "Appointment",
        "cancelation_reason_text": None,
        "appointment_type_text": None,
        "status": "booked",
        "priority": 5,
        "description": "Discussion on the results of your recent MRI",
        "start": "2013-12-10T09:00:00Z",
        "end": "2013-12-10T11:00:00Z",
        "minutes_duration": None,
        "created": "2013-10-10",
        "comment": "Further expand on the results of the MRI and determine the next actions that may be appropriate.",
        "patient_instruction": None,
    }
]


class AppointmentTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource, which is None
          for this resource.

        transformer (class): The transformer class used for transforming the
          FHIR resource.

        expected_table_name (str): The expected name of the table after transformation.
    """

    resource_type = "Appointment"
    resource_subtype = None
    transformer = AppointmentTransformer
    expected_table_name = "appointment"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
