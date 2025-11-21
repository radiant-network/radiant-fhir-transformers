"""
Test helper class for FHIR resource type Encounter subtype ReasonCode
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_reason_code import (
    EncounterReasonCodeTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_code_coding": None,
        "reason_code_text": "The patient seems to suffer from bilateral pneumonia and renal insufficiency, most likely due to chemotherapy.",
        "id": "8c7cc68b-00c0-4434-bc47-9f5b94c76479",
        "encounter_id": "f203",
    },
]


class EncounterReasonCodeTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'reason_code'.

        transformer (class): The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the table where the transformed data is expected to be stored.
    """

    resource_type = "Encounter"
    resource_subtype = "reason_code"
    transformer = EncounterReasonCodeTransformer
    expected_table_name = "encounter_reason_code"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
