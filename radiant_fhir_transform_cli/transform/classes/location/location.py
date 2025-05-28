"""
FHIR Location transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"fhir_key": "id", "type": "str"}},
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"}
        },
    },
    {
        "fhir_path": "status",
        "columns": {"status": {"fhir_key": "status", "type": "str"}},
    },
    {
        "fhir_path": "operationalStatus",
        "columns": {
            "operational_status_system": {"fhir_key": "system", "type": "str"},
            "operational_status_code": {"fhir_key": "code", "type": "str"},
            "operational_status_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "name",
        "columns": {"name": {"fhir_key": "name", "type": "str"}},
    },
    {
        "fhir_path": "description",
        "columns": {"description": {"fhir_key": "description", "type": "str"}},
    },
    {
        "fhir_path": "mode",
        "columns": {"mode": {"fhir_key": "mode", "type": "str"}},
    },
    {
        "fhir_path": "address",
        "columns": {
            "address_use": {"fhir_key": "use", "type": "str"},
            "address_type": {"fhir_key": "type", "type": "str"},
            "address_text": {"fhir_key": "text", "type": "str"},
            "address_line": {"fhir_key": "line", "type": "str"},
            "address_city": {"fhir_key": "city", "type": "str"},
            "address_district": {"fhir_key": "district", "type": "str"},
            "address_state": {"fhir_key": "state", "type": "str"},
            "address_postal_code": {"fhir_key": "postalCode", "type": "str"},
            "address_country": {"fhir_key": "country", "type": "str"},
            "address_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "address_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
    {
        "fhir_path": "physicalType.text",
        "columns": {"physical_type_text": {"fhir_key": "text", "type": "str"}},
    },
    {
        "fhir_path": "position",
        "columns": {
            "position_longitude": {"fhir_key": "longitude", "type": "str"},
            "position_latitude": {"fhir_key": "latitude", "type": "str"},
            "position_altitude": {"fhir_key": "altitude", "type": "str"},
        },
    },
    {
        "fhir_path": "managingOrganization",
        "fhir_reference": "managing_organization_reference",
        "columns": {
            "managing_organization_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "managing_organization_type": {"fhir_key": "type", "type": "str"},
            "managing_organization_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
    {
        "fhir_path": "partOf",
        "fhir_reference": "part_of_reference",
        "columns": {
            "part_of_reference": {"fhir_key": "reference", "type": "str"},
            "part_of_type": {"fhir_key": "type", "type": "str"},
            "part_of_display": {"fhir_key": "display", "type": "str"},
        },
    },
    {
        "fhir_path": "availabilityExceptions",
        "columns": {
            "availability_exceptions": {
                "fhir_key": "availabilityExceptions",
                "type": "str",
            }
        },
    },
]


class LocationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Location' resource in FHIR.

    Transform Location JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the LocationTransformer instance with the resource
            type 'Location' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Location", None, TRANSFORM_SCHEMA)
