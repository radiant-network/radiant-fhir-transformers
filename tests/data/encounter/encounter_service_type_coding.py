"""
Test helper class for FHIR resource type Encounter subtype Service Type Coding
"""

from radiant_fhir_transform_cli.transform.classes.encounter import (
    EncounterServiceTypeCodingTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "service_type_coding_system": None,
        "service_type_coding_code": None,
        "service_type_coding_display": "test",
    }
]


class EncounterServiceTypeCodingTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource subtype Service Type Coding.
    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource subtype Service Type Coding.
    It predefines the resource type as 'Encounter'
    and initializes the resource with the specific 'Encounter' resource payload
    and its expected transformation output.
    """

    resource_type = "Encounter"
    resource_subtype = "service_type_coding"
    transformer = EncounterServiceTypeCodingTransformer
    expected_table_name = "encounter_service_type_coding"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
