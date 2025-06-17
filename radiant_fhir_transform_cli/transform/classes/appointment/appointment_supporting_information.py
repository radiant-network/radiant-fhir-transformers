"""
FHIR Appointment Supporting Information transformer
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
        "fhir_path": "supportingInformation",
        "columns": {
            "supporting_information_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "supporting_information_type": {"fhir_key": "type", "type": "str"},
            "supporting_information_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class AppointmentSupportingInformationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Appointment' resource in FHIR, focusing on the 'supportingInformation' element.

    This class transforms FHIR Appointment JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'supportingInformation' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Appointment').
        subtype (str): Specifies the sub-element of the resource to focus on ('supporting_information').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the AppointmentSupportingInformationTransformer instance with the resource type 'Appointment',
            subtype 'supporting_information', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Appointment", "supporting_information", TRANSFORM_SCHEMA
        )
