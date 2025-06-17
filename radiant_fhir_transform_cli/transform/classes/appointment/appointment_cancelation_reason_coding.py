"""
FHIR Appointment Cancelation Reason Coding transformer
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
        "fhir_path": "cancelationReason.coding",
        "columns": {
            "cancelation_reason_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "cancelation_reason_coding_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "cancelation_reason_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class AppointmentCancelationReasonCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'cancelationReason.coding' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'cancelationReason.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('cancelation_reason_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentCancelationReasonCodingTransformer instance with the resource type 'Appointment',
            subtype 'cancelation_reason_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Appointment", "cancelation_reason_coding", TRANSFORM_SCHEMA
        )
