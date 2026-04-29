"""FHIR Encounter hospitalization transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Encounter",
    "name": "encounter_hospitalization",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "encounter_id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
                {
                    "name": "hospitalization_pre_admission_identifier_type_text",
                    "path": "hospitalization.preAdmissionIdentifier.type.text",
                    "type": "string",
                },
                {
                    "name": "hospitalization_pre_admission_identifier_use",
                    "path": "hospitalization.preAdmissionIdentifier.use",
                    "type": "string",
                },
                {
                    "name": "hospitalization_pre_admission_identifier_system",
                    "path": "hospitalization.preAdmissionIdentifier.system",
                    "type": "string",
                },
                {
                    "name": "hospitalization_pre_admission_identifier_value",
                    "path": "hospitalization.preAdmissionIdentifier.value",
                    "type": "string",
                },
                {
                    "name": "hospitalization_pre_admission_identifier_period_start",
                    "path": "hospitalization.preAdmissionIdentifier.period.start",
                    "type": "dateTime",
                },
                {
                    "name": "hospitalization_pre_admission_identifier_period_end",
                    "path": "hospitalization.preAdmissionIdentifier.period.end",
                    "type": "dateTime",
                },
                {
                    "name": "hospitalization_origin_reference",
                    "path": "hospitalization.origin.reference",
                    "type": "string",
                },
                {
                    "name": "hospitalization_origin_type",
                    "path": "hospitalization.origin.type",
                    "type": "string",
                },
                {
                    "name": "hospitalization_origin_display",
                    "path": "hospitalization.origin.display",
                    "type": "string",
                },
                {
                    "name": "hospitalization_admit_source_coding",
                    "path": "hospitalization.admitSource.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "hospitalization_admit_source_text",
                    "path": "hospitalization.admitSource.text",
                    "type": "string",
                },
                {
                    "name": "hospitalization_readmission_coding",
                    "path": "hospitalization.reAdmission.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "hospitalization_readmission_text",
                    "path": "hospitalization.reAdmission.text",
                    "type": "string",
                },
                {
                    "name": "hospitalization_diet_preference",
                    "path": "hospitalization.dietPreference",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "hospitalization_special_courtesy",
                    "path": "hospitalization.specialCourtesy",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "hospitalization_special_arrangement",
                    "path": "hospitalization.specialArrangement",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "hospitalization_destination_reference",
                    "path": "hospitalization.destination.reference",
                    "type": "string",
                },
                {
                    "name": "hospitalization_destination_type",
                    "path": "hospitalization.destination.type",
                    "type": "string",
                },
                {
                    "name": "hospitalization_destination_display",
                    "path": "hospitalization.destination.display",
                    "type": "string",
                },
                {
                    "name": "hospitalization_discharge_disposition_coding",
                    "path": "hospitalization.dischargeDisposition.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "hospitalization_discharge_disposition_text",
                    "path": "hospitalization.dischargeDisposition.text",
                    "type": "string",
                },
            ],
        },
    ],
}


class EncounterHospitalizationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Encounter", "hospitalization", VIEW_DEFINITION)
