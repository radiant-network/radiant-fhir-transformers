"""
Test helper class for FHIR resource type Encounter subtype diagnosis
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_diagnosis import (
    EncounterDiagnosisTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE

EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "diagnosis_condition_reference": "Condition/stroke",
        "diagnosis_condition_type": None,
        "diagnosis_condition_display": None,
        "diagnosis_use_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                "code": "AD",
                "display": "Admission diagnosis",
            }
        ],
        "diagnosis_use_text": None,
        "diagnosis_rank": 1,
    },
    {
        "encounter_id": "f203",
        "diagnosis_condition_reference": "Condition/f201",
        "diagnosis_condition_type": None,
        "diagnosis_condition_display": None,
        "diagnosis_use_coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                "code": "DD",
                "display": "Discharge diagnosis",
            }
        ],
        "diagnosis_use_text": None,
        "diagnosis_rank": None,
    },
]


class EncounterDiagnosisTestHelper(FhirResourceTestHelper):
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

        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'diagnosis'.

        transformer (class): The transformer class used for transforming the FHIR resource.

        expected_table_name (str): The name of the table where the transformed data is expected to be stored.
    """

    resource_type = "Encounter"
    resource_subtype = "diagnosis"
    transformer = EncounterDiagnosisTransformer
    expected_table_name = "encounter_diagnosis"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
