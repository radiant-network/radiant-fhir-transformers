"""
Test helper class for FHIR resource type Encounter subtype reasonReference
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_reason_reference import (
    EncounterReasonReferenceTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "reason_reference_reference": "Condition/example",
        "reason_reference_type": None,
        "reason_reference_display": None,
        "id": "cf09befd-8602-48e3-aed8-473f7c1ec276",
        "encounter_id": "f203",
    },
]


class EncounterReasonReferenceTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'reason_reference'.

        transformer (class): The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the table where the transformed data is expected to be stored.
    """

    resource_type = "Encounter"
    resource_subtype = "reason_reference"
    transformer = EncounterReasonReferenceTransformer
    expected_table_name = "encounter_reason_reference"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
