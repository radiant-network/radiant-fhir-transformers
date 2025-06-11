"""
Fhir Encounter Appointment Transformer
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
        "fhir_path": "appointment",
        "columns": {
            "appointment_reference": {"fhir_key": "reference", "type": "str"},
            "appointment_type": {"fhir_key": "type", "type": "str"},
            "appointment_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class EncounterAppointmentTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Encounter' FHIR resource, specifically for the 'appointment' field.

    This class transforms FHIR Encounter JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'appointment' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed, which is set to 'Encounter'.
        resource_subtype (str): The subtype of the FHIR resource being transformed, set to 'appointment'.
        transform_schema (list): A list of dictionaries defining how to transform the FHIR data.

    Methods:
        __init__(self):
            Initializes the EncounterAppointmentTransformer instance with the resource type 'Encounter',
            the resource subtype 'appointment', and the transformation schema.
    """

    def __init__(self):
        super().__init__("Encounter", "appointment", TRANSFORM_SCHEMA)
