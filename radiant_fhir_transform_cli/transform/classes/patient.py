"""
FHIR Patient transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

RACE_EXTENSION = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
ETHNICITY_EXTENSION = (
    "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
)

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {"id": {"fhir_key": "id", "type": "str"}},
    },
    {
        "fhir_path": "identifier.where(type.text = 'EPI').value",
        "columns": {
            "identifier_mrn": {
                "fhir_key": "identifier.where(type.text = 'EPI').value",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": f"extension.where(url = '{RACE_EXTENSION}').extension.where(url = 'text').valueString",
        "columns": {
            "race": {
                "fhir_key": f"extension.where(url = '{RACE_EXTENSION}').extension.where(url = 'text').valueString",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": f"extension.where(url = '{ETHNICITY_EXTENSION}').extension.where(url = 'text').valueString",
        "columns": {
            "ethnicity": {
                "fhir_key": f"extension.where(url = '{ETHNICITY_EXTENSION}').extension.where(url = 'text').valueString",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "name.where(use='official').given.first()",
        "columns": {
            "given_name": {
                "fhir_key": "name.where(use='official').given.first()",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "name.where(use='official').family",
        "columns": {
            "family_name": {
                "fhir_key": "name.where(use='official').given.first()",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "active",
        "columns": {"active": {"fhir_key": "active", "type": "str"}},
    },
    {
        "fhir_path": "birthDate",
        "columns": {"birth_date": {"fhir_key": "birthDate", "type": "str"}},
    },
    {
        "fhir_path": "gender",
        "columns": {"gender": {"fhir_key": "gender", "type": "str"}},
    },
    {
        "fhir_path": "deceasedBoolean",
        "columns": {
            "deceased_boolean": {"fhir_key": "deceasedBoolean", "type": "bool"}
        },
    },
    {
        "fhir_path": "deceasedDateTime",
        "columns": {
            "deceased_date_time": {
                "fhir_key": "deceasedDateTime",
                "type": "datetime",
            }
        },
    },
    {
        "fhir_path": "address.where(use='home').line.first()",
        "columns": {
            "address_line": {
                "fhir_key": "address.where(use='home').line.first()",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "address.where(use='home').city",
        "columns": {
            "address_city": {
                "fhir_key": "address.where(use='home').city",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "address.where(use='home').state",
        "columns": {
            "address_state": {
                "fhir_key": "address.where(use='home').state",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "address.where(use='home').postalCode",
        "columns": {
            "address_postal_code": {
                "fhir_key": "address.where(use='home').postalCode",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "address.where(use='home').country",
        "columns": {
            "address_country": {
                "fhir_key": "address.where(use='home').country",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "communication.where(preferred=true).language.text",
        "columns": {
            "communication_language": {
                "fhir_key": "communication.where(preferred=true).language.text",
                "type": "str",
            }
        },
    },
    {
        "fhir_path": "Patient",
        "columns": {
            "patient_raw_json": {
                "type": "str",
            }
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
        transform_schema (list[dict]): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the PatientTransformer instance with the resource
            type 'Patient' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Patient", None, TRANSFORM_SCHEMA)
