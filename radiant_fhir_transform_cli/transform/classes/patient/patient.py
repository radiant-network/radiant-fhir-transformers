"""FHIR Patient transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient",
    "status": "active",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id", "type": "string"},
                {
                    "name": "identifier_mrn",
                    "path": "identifier.where(type.text = 'EPI').value",
                    "type": "string",
                },
                {
                    "name": "race",
                    "path": "extension.where(url = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-race').extension.where(url = 'text').valueString",
                    "type": "string",
                },
                {
                    "name": "ethnicity",
                    "path": "extension.where(url = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity').extension.where(url = 'text').valueString",
                    "type": "string",
                },
                {
                    "name": "given_name",
                    "path": "name.where(use='official').given.first()",
                    "type": "string",
                },
                {
                    "name": "family_name",
                    "path": "name.where(use='official').family",
                    "type": "string",
                },
                {"name": "active", "path": "active", "type": "string"},
                {"name": "birth_date", "path": "birthDate", "type": "string"},
                {"name": "gender", "path": "gender", "type": "string"},
                {
                    "name": "deceased_boolean",
                    "path": "deceasedBoolean",
                    "type": "string",
                },
                {
                    "name": "deceased_date_time",
                    "path": "deceasedDateTime",
                    "type": "dateTime",
                },
                {
                    "name": "address_line",
                    "path": "address.where(use='home').line.first()",
                    "type": "string",
                },
                {
                    "name": "address_city",
                    "path": "address.where(use='home').city",
                    "type": "string",
                },
                {
                    "name": "address_state",
                    "path": "address.where(use='home').state",
                    "type": "string",
                },
                {
                    "name": "address_postal_code",
                    "path": "address.where(use='home').postalCode",
                    "type": "string",
                },
                {
                    "name": "address_country",
                    "path": "address.where(use='home').country",
                    "type": "string",
                },
                {
                    "name": "communication_language",
                    "path": "communication.where(preferred=true).language.text",
                    "type": "string",
                },
            ]
        }
    ],
}


class PatientTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", None, VIEW_DEFINITION)
