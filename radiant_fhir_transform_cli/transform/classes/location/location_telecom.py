"""
FHIR Location Telecom transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
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
            "location_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "telecom",
        "columns": {
            "telecom_system": {"fhir_key": "system", "type": "str"},
            "telecom_value": {"fhir_key": "value", "type": "str"},
            "telecom_use": {"fhir_key": "use", "type": "str"},
            "telecom_rank": {"fhir_key": "rank", "type": "int"},
            "telecom_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "telecom_period_end": {
                "fhir_key": "period.end",
                "type": "datetime",
            },
        },
    },
]


class LocationTelecomTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Location' resource in FHIR, focusing on the 'telecom' element.
    This class transforms FHIR Location JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'telecom' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Location').
        subtype (str): Specifies the sub-element of the resource to focus on ('telecom').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the LocationTelecomTransformer instance with the resource type 'Location',
            subtype 'telecom', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Location", "telecom", TRANSFORM_SCHEMA)
