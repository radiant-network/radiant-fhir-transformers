"""
FHIR Location HoursOfOperation transformer
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
        "fhir_path": "hoursOfOperation",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "hours_of_operation_days_of_week": {
                "fhir_key": "daysOfWeek",
                "type": "str",
            },
            "hours_of_operation_all_day": {
                "fhir_key": "allDay",
                "type": "bool",
            },
            "hours_of_operation_opening_time": {
                "fhir_key": "openingTime",
                "type": "str",
            },
            "hours_of_operation_closing_time": {
                "fhir_key": "closingTime",
                "type": "str",
            },
        },
    },
]


class LocationHoursOfOperationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Location' resource in FHIR, focusing on the 'hoursOfOperation' element.
    This class transforms FHIR Location JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'hoursOfOperation' field.
    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Location').
        subtype (str): Specifies the sub-element of the resource to focus on ('hours_of_operation').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.
    Methods:
        __init__():
            Initializes the LocationHoursOfOperationTransformer instance with the resource type 'Location',
            subtype 'hours_of_operation', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Location", "hours_of_operation", TRANSFORM_SCHEMA)
