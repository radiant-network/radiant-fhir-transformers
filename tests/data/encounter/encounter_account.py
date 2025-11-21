"""
Test helper class for FHIR resource type Encounter subtype account
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_account import (
    EncounterAccountTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "account_reference": "Account/example",
        "account_type": None,
        "account_display": None,
        "id": "bf04b48d-c79c-4b92-ae78-3467102e82c7",
        "encounter_id": "f203",
    },
]


class EncounterAccountTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource.

    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.

        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'account'.
        resource (dict): The FHIR Encounter resource payload to be transformed.
        expected_output (list): The expected output after transformation of the FHIR resource.
        transformer_class (type): The class responsible for transforming the FHIR resource.
    """

    resource_type = "Encounter"
    resource_subtype = "account"
    transformer = EncounterAccountTransformer
    expected_table_name = "encounter_account"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
