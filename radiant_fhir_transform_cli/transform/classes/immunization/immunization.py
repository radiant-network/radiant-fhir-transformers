"""
FHIR Immunization transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"},
        },
    },
    {
        "fhir_path": "status",
        "columns": {
            "status": {"fhir_key": "status", "type": "str"},
        },
    },
    {
        "fhir_path": "statusReason.text",
        "columns": {
            "status_reason_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "vaccineCode.text",
        "columns": {
            "vaccine_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "patient",
        "fhir_reference": "patient_reference",
        "columns": {
            "patient_reference": {"fhir_key": "reference", "type": "str"},
            "patient_type": {"fhir_key": "type", "type": "str"},
            "patient_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "encounter",
        "fhir_reference": "encounter_reference",
        "columns": {
            "encounter_reference": {"fhir_key": "reference", "type": "str"},
            "encounter_type": {"fhir_key": "type", "type": "str"},
            "encounter_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "occurrenceDateTime",
        "columns": {
            "occurrence_date_time": {
                "fhir_key": "occurrenceDateTime",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "occurrenceString",
        "columns": {
            "occurrence_string": {
                "fhir_key": "occurrenceString",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "recorded",
        "columns": {
            "recorded": {"fhir_key": "recorded", "type": "datetime"},
        },
    },
    {
        "fhir_path": "primarySource",
        "columns": {
            "primary_source": {"fhir_key": "primarySource", "type": "bool"},
        },
    },
    {
        "fhir_path": "reportOrigin.text",
        "columns": {
            "report_origin_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "location",
        "fhir_reference": "location_reference",
        "columns": {
            "location_reference": {"fhir_key": "reference", "type": "str"},
            "location_type": {"fhir_key": "type", "type": "str"},
            "location_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "manufacturer",
        "fhir_reference": "manufacturer_reference",
        "columns": {
            "manufacturer_reference": {"fhir_key": "reference", "type": "str"},
            "manufacturer_type": {"fhir_key": "type", "type": "str"},
            "manufacturer_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "lotNumber",
        "columns": {
            "lot_number": {"fhir_key": "lotNumber", "type": "str"},
        },
    },
    {
        "fhir_path": "expirationDate",
        "columns": {
            "expiration_date": {
                "fhir_key": "expirationDate",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "site.text",
        "columns": {
            "site_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "route.text",
        "columns": {
            "route_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "doseQuantity",
        "columns": {
            "dose_quantity_value": {"fhir_key": "value", "type": "str"},
            "dose_quantity_unit": {"fhir_key": "unit", "type": "str"},
            "dose_quantity_system": {"fhir_key": "system", "type": "str"},
            "dose_quantity_code": {"fhir_key": "code", "type": "str"},
        },
    },
    {
        "fhir_path": "isSubpotent",
        "columns": {
            "is_subpotent": {"fhir_key": "isSubpotent", "type": "bool"},
        },
    },
    {
        "fhir_path": "fundingSource.text",
        "columns": {
            "funding_source_text": {"fhir_key": "text", "type": "str"},
        },
    },
    {
        "fhir_path": "Immunization",
        "columns": {
            "immunization_raw_json": {
                "type": "str",
            }
        },
    },
]


class ImmunizationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR.

    Transform Immunization JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the Immunizationformer instance with the resource
            type 'Immunization' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", None, TRANSFORM_SCHEMA)
