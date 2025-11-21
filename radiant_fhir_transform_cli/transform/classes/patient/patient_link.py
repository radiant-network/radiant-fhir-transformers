"""FHIR Patient link transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Patient",
    "name": "patient_link",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "patient_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "link",
            "column": [
                {
                    "name": "link_other_reference",
                    "path": "other.reference",
                    "type": "string",
                },
                {
                    "name": "link_other_type",
                    "path": "other.type",
                    "type": "string",
                },
                {
                    "name": "link_other_identifier",
                    "path": "other.identifier",
                    "type": "string",
                },
                {
                    "name": "link_other_display",
                    "path": "other.display",
                    "type": "string",
                },
                {
                    "name": "link_type",
                    "path": "type",
                    "type": "string",
                },
            ],
        },
    ],
}


class PatientLinkTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Patient", "link", VIEW_DEFINITION)
