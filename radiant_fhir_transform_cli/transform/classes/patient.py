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
    FhirResourceTransformer,
)

RACE_EXTENSION = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
ETHNICITY_EXTENSION = (
    "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
)

TRANSFORM_DICT = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": "id",
        },
    },
    {
        "fhir_path": "identifier.where(type.text = 'EPI').value",
        "columns": {
            "identifier_mrn": "identifier.where(type.text = 'EPI').value",
        },
    },
    {
        "fhir_path": f"extension.where(url = '{RACE_EXTENSION}').extension.where(url = 'text').valueString",
        "columns": {
            "race": f"extension.where(url = '{RACE_EXTENSION}').extension.where(url = 'text').valueString",
        },
    },
    {
        "fhir_path": f"extension.where(url = '{ETHNICITY_EXTENSION}').extension.where(url = 'text').valueString",
        "columns": {
            "ethnicity": f"extension.where(url = '{ETHNICITY_EXTENSION}').extension.where(url = 'text').valueString",
        },
    },
    {
        "fhir_path": "name.where(use='official').given.first()",
        "columns": {
            "given_name": "name.where(use='official').given.first()",
        },
    },
    {
        "fhir_path": "name.where(use='official').family",
        "columns": {
            "family_name": "name.where(use='official').given.first()",
        },
    },
    {
        "fhir_path": "active",
        "columns": {
            "active": "active",
        },
    },
    {
        "fhir_path": "birthDate",
        "columns": {
            "birth_date": "birthDate",
        },
    },
    {
        "fhir_path": "gender",
        "columns": {
            "gender": "gender",
        },
    },
    {
        "fhir_path": "deceasedBoolean",
        "columns": {
            "deceased_boolean": "deceasedBoolean",
        },
    },
    {
        "fhir_path": "deceasedDateTime",
        "columns": {
            "deceased_date_time": "deceasedDateTime",
        },
    },
    {
        "fhir_path": "address.where(use='home').line.first()",
        "columns": {
            "address_line": "address.where(use='home').line.first()",
        },
    },
    {
        "fhir_path": "address.where(use='home').city",
        "columns": {
            "address_city": "address.where(use='home').city",
        },
    },
    {
        "fhir_path": "address.where(use='home').state",
        "columns": {
            "address_state": "address.where(use='home').state",
        },
    },
    {
        "fhir_path": "address.where(use='home').postalCode",
        "columns": {
            "address_postal_code": "address.where(use='home').postalCode",
        },
    },
    {
        "fhir_path": "address.where(use='home').country",
        "columns": {
            "address_country": "address.where(use='home').country",
        },
    },
    {
        "fhir_path": "communication.where(preferred=true).language.text",
        "columns": {
            "communication_language": "communication.where(preferred=true).language.text",
        },
    },
]


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
        super().__init__("Patient", None, TRANSFORM_DICT)
