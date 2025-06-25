"""
FHIR Appointment Requested Period transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "appointment_id": {"type": "str"},
        },
    },
    {
        "fhir_path": "requestedPeriod",
        "columns": {
            "requested_period_start": {"fhir_key": "start", "type": "datetime"},
            "requested_period_end": {"fhir_key": "end", "type": "datetime"},
        },
    },
]


class AppointmentRequestedPeriodTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'requestedPeriod' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'requestedPeriod' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('requested_period').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentRequestedPeriodTransformer instance with the resource type 'Appointment',
            subtype 'requested_period', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", "requested_period", TRANSFORM_SCHEMA)
