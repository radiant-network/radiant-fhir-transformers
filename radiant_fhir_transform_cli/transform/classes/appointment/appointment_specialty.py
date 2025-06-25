"""
FHIR Appointment Specialty transformer
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
        "fhir_path": "specialty",
        "columns": {
            "specialty_coding": {"fhir_key": "coding", "type": "str"},
            "specialty_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class AppointmentSpecialtyTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'specialty' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'specialty' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('specialty').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentspecialtyTransformer instance with the resource type 'Appointment',
            subtype 'specialty', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", "specialty", TRANSFORM_SCHEMA)
