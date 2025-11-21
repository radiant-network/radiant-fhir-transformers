"""
Test helper class for FHIR resource type Organization subtype Name
"""

from radiant_fhir_transform_cli.transform.classes.patient import (
    PatientNameTransformer,
)
from tests.data.base import FhirResourceTestHelper

from .patient import RESOURCE

EXPECTED_OUTPUT = [
    {
        "name_given": "Betty",
        "name_use": "official",
        "name_text": "Betty MyChart",
        "name_family": "MyChart",
        "name_prefix": None,
        "name_suffix": None,
        "name_period_start": None,
        "name_period_end": None,
        "id": "832075b4-1917-4916-a076-be26ce4b9c7c",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "name_given": "Elizabeth",
        "name_use": "official",
        "name_text": "Betty MyChart",
        "name_family": "MyChart",
        "name_prefix": None,
        "name_suffix": None,
        "name_period_start": None,
        "name_period_end": None,
        "id": "14092221-fc54-47a3-8db0-0e29b8a85d6b",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "name_given": "Betty",
        "name_use": "usual",
        "name_text": "Betty MyChart",
        "name_family": "MyChart",
        "name_prefix": None,
        "name_suffix": None,
        "name_period_start": None,
        "name_period_end": None,
        "id": "4392bd68-2be0-483e-afcf-6cb0defd74cc",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
    {
        "name_given": "Betty",
        "name_use": "old",
        "name_text": "MYCHARTADMIN,BETTY",
        "name_family": "Mychartadmin",
        "name_prefix": None,
        "name_suffix": None,
        "name_period_start": None,
        "name_period_end": None,
        "id": "a1addaa8-eb3b-49db-9d92-8e45bf1fa762",
        "patient_id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    },
]


class PatientNameTestHelper(FhirResourceTestHelper):
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
    resource_subtype = "name"
    transformer = PatientNameTransformer
    expected_table_name = "patient_name"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
