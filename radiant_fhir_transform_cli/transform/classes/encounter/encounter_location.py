"""
FHIR Encounter Location Transformer Class
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
        "fhir_path": "location",
        "columns": {
            "location_location_reference": {
                "fhir_key": "location.reference",
                "type": "str",
            },
            "location_location_type": {
                "fhir_key": "location.type",
                "type": "str",
            },
            "location_location_display": {
                "fhir_key": "location.display",
                "type": "str",
            },
            "location_status": {"fhir_key": "status", "type": "str"},
            "location_physical_type_coding_code": {
                "fhir_key": "physicalType.coding.code",
                "type": "str",
            },
            "location_physical_type_coding_system": {
                "fhir_key": "physicalType.coding.system",
                "type": "str",
            },
            "location_physical_type_coding_display": {
                "fhir_key": "physicalType.coding.display",
                "type": "str",
            },
            "location_physical_type_text": {
                "fhir_key": "physicalType.text",
                "type": "str",
            },
            "location_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "location_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class EncounterLocationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'location' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'location' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'location'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.

    Methods:
    __init__():
        Initializes the EncounterLocationTransformer instance with the resource type 'Encounter',
        subtype 'location', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Encounter", "location", TRANSFORM_SCHEMA)
