"""
FHIR Patient transformer

Map nested fields in the Patient resource to keys in a flat dict which
represents a row in a csv file

Transform Dictionary
--------------------
- Keys are output columns in a csv file.

- Values are FHIR path expressions to
  the field value to be extracted from the FHIR JSON object
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer
)


TRANSFORM_DICT = {
    "given_name": "name.where(use='official').given.first()",
    "family_name": "name.where(use='official').family",
    "active": "active",
    "birth_date": "birthDate",
    "gender": "gender",
}


class PatientTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Patient' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file


    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the PatientTransformer instance with the resource
            type 'Patient' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Patient", TRANSFORM_DICT)
