"""FHIR Specimen note transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_note",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "specimen_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "note",
            "column": [
                {"name": "note_text", "path": "text", "type": "string"},
                {
                    "name": "note_author_string",
                    "path": "authorString",
                    "type": "string",
                },
                {
                    "name": "note_author_reference_reference",
                    "path": "authorReference.reference",
                    "type": "string",
                },
                {
                    "name": "note_author_reference_display",
                    "path": "authorReference.display",
                    "type": "string",
                },
                {
                    "name": "note_author_reference_type",
                    "path": "authorReference.type",
                    "type": "string",
                },
                {"name": "note_time", "path": "time", "type": "dateTime"},
            ],
        },
    ],
}


class SpecimenNoteTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "note", VIEW_DEFINITION)
