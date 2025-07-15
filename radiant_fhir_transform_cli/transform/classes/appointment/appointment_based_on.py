"""
FHIR Appointment Based On transformer
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
        "fhir_path": "basedOn",
        "columns": {
            "based_on_reference": {"fhir_key": "reference", "type": "str"},
            "based_on_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class AppointmentBasedOnTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'basedOn' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'basedOn' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('based_on').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentBasedOnTransformer instance with the resource type 'Appointment',
            subtype 'based_on', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", "based_on", TRANSFORM_SCHEMA)
