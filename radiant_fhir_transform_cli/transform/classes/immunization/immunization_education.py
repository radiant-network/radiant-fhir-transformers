"""
FHIR Immunization Education transformer
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
            "immunization_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "education",
        "columns": {
            "education_document_type": {
                "fhir_key": "documentType",
                "type": "str",
            },
            "education_reference": {"fhir_key": "reference", "type": "str"},
            "education_publication_date": {
                "fhir_key": "publicationDate",
                "type": "datetime",
            },
            "education_presentation_date": {
                "fhir_key": "presentationDate",
                "type": "datetime",
            },
        },
    },
]


class ImmunizationEducationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Immunization' resource in FHIR, focusing on the 'education' element.

    This class transforms FHIR Immunization JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'education' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Immunization').
        subtype (str): Specifies the sub-element of the resource to focus on ('education').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ImmunizationEducationTransformer instance with the resource type 'Immunization',
            subtype 'education', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Immunization", "education", TRANSFORM_SCHEMA)
