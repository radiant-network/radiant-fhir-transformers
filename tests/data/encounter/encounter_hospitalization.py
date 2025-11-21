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
        "hospitalization_special_arrangement_text": None,
        "hospitalization_special_arrangement_coding_system": "http://terminology.hl7.org/CodeSystem/encounter-special-arrangements",
        "hospitalization_special_arrangement_coding_code": "wheel",
        "hospitalization_special_arrangement_coding_display": "Wheelchair",
        "hospitalization_special_courtesy_text": None,
        "hospitalization_special_courtesy_coding_system": "http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCourtesy",
        "hospitalization_special_courtesy_coding_code": "NRM",
        "hospitalization_special_courtesy_coding_display": "normal courtesy",
        "hospitalization_diet_preference_text": None,
        "hospitalization_diet_preference_coding_system": "http://snomed.info/sct",
        "hospitalization_diet_preference_coding_code": "276026009",
        "hospitalization_diet_preference_coding_display": "Fluid balance regulation",
        "hospitalization_readmission_coding_display": "readmitted",
        "hospitalization_admit_source_coding_system": "http://snomed.info/sct",
        "hospitalization_admit_source_coding_code": "309902002",
        "hospitalization_admit_source_coding_display": "Clinical Oncology Department",
        "encounter_id": "f203",
        "id": "4c082a10-9117-4276-a9fe-a6b462b31579",
        "hospitalization_pre_admission_identifier_type_text": None,
        "hospitalization_pre_admission_identifier_use": None,
        "hospitalization_pre_admission_identifier_system": None,
        "hospitalization_pre_admission_identifier_value": None,
        "hospitalization_pre_admission_identifier_period_start": None,
        "hospitalization_pre_admission_identifier_period_end": None,
        "hospitalization_origin_reference": "Location/2",
        "hospitalization_origin_type": None,
        "hospitalization_origin_display": None,
        "hospitalization_admit_source_text": None,
        "hospitalization_readmission_text": None,
        "hospitalization_destination_reference": "Location/2",
        "hospitalization_destination_type": None,
        "hospitalization_destination_display": None,
        "hospitalization_discharge_disposition_coding": None,
        "hospitalization_discharge_disposition_text": None,
    },
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
