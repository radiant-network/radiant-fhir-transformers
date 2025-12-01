"""FHIR Immunization education transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_education",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "immunization_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "education",
            "column": [
                {
                    "name": "education_document_type",
                    "path": "documentType",
                    "type": "string",
                },
                {
                    "name": "education_reference",
                    "path": "reference",
                    "type": "string",
                },
                {
                    "name": "education_publication_date",
                    "path": "publicationDate",
                    "type": "dateTime",
                },
                {
                    "name": "education_presentation_date",
                    "path": "presentationDate",
                    "type": "dateTime",
                },
            ],
        },
    ],
}


class ImmunizationEducationTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "education", VIEW_DEFINITION)
