"""
Test helper class for FHIR resource type Organization subtype Telecom
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientTelecomTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient import RESOURCE

EXPECTED_OUTPUT = [
    {
        "patient_id":"e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "telecom_system": "phone",
        "telecom_value": "610-357-7956",
        "telecom_use": "mobile",
        "telecom_rank": 1,
        "telecom_period_start": None,
        "telecom_period_end": None,
    },
    {
        "patient_id":"e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        "telecom_system": "email",
        "telecom_value": "hakp@email.chop.edu",
        "telecom_use": None,
        "telecom_rank": 1,
        "telecom_period_start": None,
        "telecom_period_end": None,
    },
]


class PatientTelecomTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Patient' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Patient' resource.

    It predefines the resource type as 'Patient'
    and initializes the resource with the specific 'Patient' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Patient'.

        resource (dict): The raw FHIR 'Patient' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Patient' resource payload.
    """

    resource_type = "Patient"
    resource_subtype = "telecom"
    transformer = PatientTelecomTransformer
    expected_table_name = "patient_telecom"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
