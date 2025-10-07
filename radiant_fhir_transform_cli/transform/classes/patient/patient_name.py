"""
FHIR Patient Name transformer
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
        "fhir_path": "name",
        "columns": {
            "name_use": {"fhir_key": "use", "type": "str"},
            "name_text": {"fhir_key": "text", "type": "str"},
            "name_family": {"fhir_key": "family", "type": "str"},
            "name_given": {"fhir_key": "given", "type": "str"},
            "name_prefix": {"fhir_key": "prefix", "type": "str"},
            "name_suffix": {"fhir_key": "suffix", "type": "str"},
            "name_period_start": {
                "fhir_key": "period.start",
                "type": "datetime",
            },
            "name_period_end": {"fhir_key": "period.end", "type": "datetime"},
        },
    },
]


class PatientNameTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Patient' resource in FHIR, focusing on the 'name' element.

    This class transforms FHIR Coverage JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'name' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Patient').
        subtype (str): Specifies the sub-element of the resource to focus on ('name').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the PatientNameTransformer instance with the resource type 'Patient',
            subtype 'name', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Patient", "name", TRANSFORM_SCHEMA)
