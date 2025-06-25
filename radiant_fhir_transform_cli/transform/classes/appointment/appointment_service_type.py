"""
FHIR Appointment Service Type transformer
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
        "fhir_path": "serviceType",
        "columns": {
            "service_type_coding": {"fhir_key": "coding", "type": "str"},
            "service_type_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class AppointmentServiceTypeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'serviceType' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'serviceType' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('service_type').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentServicetypeTransformer instance with the resource type 'Appointment',
            subtype 'service_type', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Appointment", "service_type", TRANSFORM_SCHEMA)
