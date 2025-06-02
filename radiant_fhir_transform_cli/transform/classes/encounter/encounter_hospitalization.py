"""
FHIR Encounter Hospitalization Transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "encounter_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "hospitalization",
        "columns": {
            # preAdmissionIdentifier
            "hospitalization_pre_admission_identifier_use": {
                "fhir_key": "preAdmissionIdentifier.use",
                "type": "str",
            },
            "hospitalization_pre_admission_identifier_system": {
                "fhir_key": "preAdmissionIdentifier.system",
                "type": "str",
            },
            "hospitalization_pre_admission_identifier_value": {
                "fhir_key": "preAdmissionIdentifier.value",
                "type": "str",
            },
            # origin
            "hospitalization_origin_reference": {
                "fhir_key": "origin.reference",
                "type": "str",
            },
            "hospitalization_origin_type": {
                "fhir_key": "origin.type",
                "type": "str",
            },
            "hospitalization_origin_display": {
                "fhir_key": "origin.display",
                "type": "str",
            },
            # admitSource
            # TODO: add support for multiple codings
            "hospitalization_admit_source_coding": {
                "fhir_key": "admitSource.coding",
                "type": "str",
            },
            "hospitalization_admit_source_text": {
                "fhir_key": "admitSource.text",
                "type": "str",
            },
            # reAdmission
            # TODO: add support for multiple codings
            "hospitalization_readmission_coding": {
                "fhir_key": "reAdmission.coding",
                "type": "str",
            },
            "hospitalization_readmission_text": {
                "fhir_key": "reAdmission.text",
                "type": "str",
            },
            # dietPreference
            # TODO: add support for multiple codings
            "hospitalization_diet_preference_coding": {
                "fhir_key": "dietPreference.coding",
                "type": "str",
            },
            "hospitalization_diet_preference_text": {
                "fhir_key": "dietPreference.text",
                "type": "str",
            },
            # specialCourtesy
            # TODO: add support for multiple codings
            "hospitalization_special_courtesy_coding": {
                "fhir_key": "specialCourtesy.coding",
                "type": "str",
            },
            "hospitalization_special_courtesy_text": {
                "fhir_key": "specialCourtesy.text",
                "type": "str",
            },
            # specialArrangement
            # TODO: add support for multiple codings
            "hospitalization_special_arrangement_coding": {
                "fhir_key": "specialArrangement.coding",
                "type": "str",
            },
            "hospitalization_special_arrangement_text": {
                "fhir_key": "specialArrangement.text",
                "type": "str",
            },
            # destination
            "hospitalization_destination_reference": {
                "fhir_key": "destination.reference",
                "type": "str",
            },
            "hospitalization_destination_type": {
                "fhir_key": "destination.type",
                "type": "str",
            },
            "hospitalization_destination_display": {
                "fhir_key": "destination.display",
                "type": "str",
            },
            # dischargeDisposition
            # TODO: add support for multiple codings
            "hospitalization_discharge_disposition_coding": {
                "fhir_key": "dischargeDisposition.coding",
                "type": "str",
            },
            "hospitalization_discharge_disposition_text": {
                "fhir_key": "dischargeDisposition.text",
                "type": "str",
            },
        },
    },
]


class EncounterHospitalizationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'hospitalization' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'hospitalization' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'hospitalization'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.
    """

    def __init__(self):
        super().__init__("Encounter", "hospitalization", TRANSFORM_SCHEMA)
