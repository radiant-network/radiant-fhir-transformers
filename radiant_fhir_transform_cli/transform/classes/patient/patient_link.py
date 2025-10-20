"""
FHIR Patient Link transformer
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
        "fhir_path": "link",
        "fhir_reference": "link_other_reference",
        "columns": {
            "link_other_reference": {
                "fhir_key": "other.reference",
                "type": "str",
            },
            "link_other_type": {"fhir_key": "other.type", "type": "str"},
            "link_other_identifier": {
                "fhir_key": "other.identifier",
                "type": "str",
            },
            "link_other_display": {"fhir_key": "other.display", "type": "str"},
            "link_type": {"fhir_key": "type", "type": "str"},
        },
    },
]


class PatientLinkTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Patient' resource in FHIR, focusing on the 'link' element.

    This class transforms FHIR Patient JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'link' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Patient').
        subtype (str): Specifies the sub-element of the resource to focus on ('link').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the PatientLinkTransformer instance with the resource type 'Patient',
            subtype 'link', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Patient", "link", TRANSFORM_SCHEMA)
