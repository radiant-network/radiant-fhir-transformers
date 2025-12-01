"""FHIR BodyStructure transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "BodyStructure",
    "name": "body_structure",
    "status": "active",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id", "type": "string"},
                {
                    "name": "resource_type",
                    "path": "resourceType",
                    "type": "string",
                },
                {"name": "active", "path": "active", "type": "string"},
                {
                    "name": "morphology_text",
                    "path": "morphology.text",
                    "type": "string",
                },
                {
                    "name": "location_text",
                    "path": "location.text",
                    "type": "string",
                },
                {
                    "name": "description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "patient_reference",
                    "path": "patient.reference",
                    "type": "string",
                },
                {
                    "name": "patient_type",
                    "path": "patient.type",
                    "type": "string",
                },
                {
                    "name": "patient_display",
                    "path": "patient.display",
                    "type": "string",
                },
            ]
        }
    ],
}


class BodyStructureTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("BodyStructure", None, VIEW_DEFINITION)
