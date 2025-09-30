"""
FHIR Patient GeneralPractitioner transformer
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
            "patient_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "generalPractitioner",
        "fhir_reference": "general_practitioner_reference",
        "columns": {
            "general_practitioner_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "general_practitioner_type": {"fhir_key": "type", "type": "str"},
            "general_practitioner_identifier": {"fhir_key": "identifier", "type": "str"},
            "general_practitioner_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class PatientGeneralPractitionerTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Patient' resource in FHIR, focusing on the 'generalPractitioner' element.

    This class transforms FHIR Patient JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'generalPractitioner' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Patient').
        subtype (str): Specifies the sub-element of the resource to focus on ('general_practitioner').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the PatientGeneralPractitionerTransformer instance with the resource type 'Patient',
            subtype 'general_practitioner', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Patient", "general_practitioner", TRANSFORM_SCHEMA)
