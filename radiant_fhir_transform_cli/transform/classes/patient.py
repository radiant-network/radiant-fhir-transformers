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

TRANSFORM_DICT = {
    "identifier_mrn": "identifier.where(type.text = 'EPI').value",
    "id": "identifier.where(type.text = 'FHIR STU3').value",
    "race": f"extension.where(url = '{RACE_EXTENSION}').extension.where(url = 'text').valueString",
    "ethnicity": f"extension.where(url = '{ETHNICITY_EXTENSION}').extension.where(url = 'text').valueString",
    "given_name": "name.where(use='official').given.first()",
    "family_name": "name.where(use='official').family",
    "active": "active",
    "birth_date": "birthDate",
    "gender": "gender",
    "deceased_boolean": "deceasedBoolean",
    "deceased_date_time": "deceasedDateTime",
    "address_line": "address.where(use='home').line.first()",
    "address_city": "address.where(use='home').city",
    "address_state": "address.where(use='home').state",
    "address_postal_code": "address.where(use='home').postalCode",
    "address_country": "address.where(use='home').country",
    "communication_language": "communication.where(preferred=true).language.text",
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
