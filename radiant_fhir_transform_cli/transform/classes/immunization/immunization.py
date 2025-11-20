"""FHIR Immunization transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization",
    "status": "active",
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                    "type": "string",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {
                    "name": "status",
                    "path": "status",
                    "type": "string",
                },
                {
                    "name": "status_reason_text",
                    "path": "statusReason.text",
                    "type": "string",
                },
                {
                    "name": "vaccine_code_text",
                    "path": "vaccineCode.text",
                    "type": "string",
                },
                {
                    "name": "patient_reference",
                    "path": "patient.reference",
                    "type": "string",
                },
                {
                    "name": "patient_type",
                    "path": "patient.type",
                    "type": "string",
                },
                {
                    "name": "patient_display",
                    "path": "patient.display",
                    "type": "string",
                },
                {
                    "name": "encounter_reference",
                    "path": "encounter.reference",
                    "type": "string",
                },
                {
                    "name": "encounter_type",
                    "path": "encounter.type",
                    "type": "string",
                },
                {
                    "name": "encounter_display",
                    "path": "encounter.display",
                    "type": "string",
                },
                {
                    "name": "occurrence_date_time",
                    "path": "occurrenceDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "occurrence_string",
                    "path": "occurrenceString",
                    "type": "string",
                },
                {
                    "name": "recorded",
                    "path": "recorded",
                    "type": "dateTime",
                },
                {
                    "name": "primary_source",
                    "path": "primarySource",
                    "type": "string",
                },
                {
                    "name": "report_origin_text",
                    "path": "reportOrigin.text",
                    "type": "string",
                },
                {
                    "name": "location_reference",
                    "path": "location.reference",
                    "type": "string",
                },
                {
                    "name": "location_type",
                    "path": "location.type",
                    "type": "string",
                },
                {
                    "name": "location_display",
                    "path": "location.display",
                    "type": "string",
                },
                {
                    "name": "manufacturer_reference",
                    "path": "manufacturer.reference",
                    "type": "string",
                },
                {
                    "name": "manufacturer_type",
                    "path": "manufacturer.type",
                    "type": "string",
                },
                {
                    "name": "manufacturer_display",
                    "path": "manufacturer.display",
                    "type": "string",
                },
                {
                    "name": "lot_number",
                    "path": "lotNumber",
                    "type": "string",
                },
                {
                    "name": "expiration_date",
                    "path": "expirationDate",
                    "type": "dateTime",
                },
                {
                    "name": "site_text",
                    "path": "site.text",
                    "type": "string",
                },
                {
                    "name": "route_text",
                    "path": "route.text",
                    "type": "string",
                },
                {
                    "name": "dose_quantity_value",
                    "path": "doseQuantity.value",
                    "type": "string",
                },
                {
                    "name": "dose_quantity_unit",
                    "path": "doseQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "dose_quantity_system",
                    "path": "doseQuantity.system",
                    "type": "string",
                },
                {
                    "name": "dose_quantity_code",
                    "path": "doseQuantity.code",
                    "type": "string",
                },
                {
                    "name": "is_subpotent",
                    "path": "isSubpotent",
                    "type": "string",
                },
                {
                    "name": "funding_source_text",
                    "path": "fundingSource.text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", None, VIEW_DEFINITION)
