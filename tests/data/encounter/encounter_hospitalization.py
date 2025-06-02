"""
Test helper class for FHIR resource type Encounter subtype hospitalization
"""

from radiant_fhir_transform_cli.transform.classes.encounter.encounter_hospitalization import (
    EncounterHospitalizationTransformer,
)
from tests.data.base import FhirResourceTestHelper
from .encounter_resource import RESOURCE
EXPECTED_OUTPUT = [
    {
        "encounter_id": "f203",
        "hospitalization_pre_admission_identifier_use": None,
        "hospitalization_pre_admission_identifier_system": None,
        "hospitalization_pre_admission_identifier_value": None,
        "hospitalization_origin_reference": "Location/2",
        "hospitalization_origin_type": None,
        "hospitalization_origin_display": None,
        "hospitalization_admit_source_coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "309902002",
                    "display": "Clinical Oncology Department",
                }
            ],
        "hospitalization_admit_source_text": None,
        "hospitalization_readmission_coding": [{"display": "readmitted"}],
        "hospitalization_readmission_text": None,
        "hospitalization_diet_preference_coding": [[{
            "system": "http://snomed.info/sct",
            "code": "276026009",
            "display": "Fluid balance regulation",
        }]],
        "hospitalization_diet_preference_text": None,
        "hospitalization_special_courtesy_coding": [[{
            "system": "http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCourtesy",
            "code": "NRM",
            "display": "normal courtesy",
        }]],
        "hospitalization_special_courtesy_text": None,
        "hospitalization_special_arrangement_coding": [[{
            "system": "http://terminology.hl7.org/CodeSystem/encounter-special-arrangements",
            "code": "wheel",
            "display": "Wheelchair",
        }]],
        "hospitalization_special_arrangement_text": None,
        "hospitalization_destination_reference": "Location/2",
        "hospitalization_destination_type": None,
        "hospitalization_destination_display": None,
        "hospitalization_discharge_disposition_coding": None,
        "hospitalization_discharge_disposition_text": None,
    }
]

class EncounterHospitalizationTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Encounter' resource,
    specifically for the 'hospitalization' subtype.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Encounter' resource
    with a focus on the 'hospitalization' field.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being tested, set to 'hospitalization'.
        transformer (type): The class responsible for transforming the FHIR resource.
        expected_table_name (str): The name of the table expected after transformation.

"""

    resource_type = "Encounter"
    resource_subtype = "hospitalization"
    transformer = EncounterHospitalizationTransformer
    expected_table_name = "encounter_hospitalization"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)