"""
FHIR Appointment Slot transformer
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
        "fhir_path": "slot",
        "columns": {
            "slot_reference": {"fhir_key": "reference", "type": "str"},
            "slot_type": {"fhir_key": "type", "type": "str"},
            "slot_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class AppointmentSlotTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'slot' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'slot' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('slot').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentSlotTransformer instance with the resource type 'Appointment',
            subtype 'slot', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", "slot", TRANSFORM_SCHEMA)
