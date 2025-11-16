"""FHIR Medication identifier transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Medication",
    "name": "medication_identifier",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "medication_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "identifier",
            "column": [
                {"name": "identifier_use", "path": "use", "type": "string"},
                {
                    "name": "identifier_system",
                    "path": "system",
                    "type": "string",
                },
                {"name": "identifier_value", "path": "value", "type": "string"},
            ],
        },
    ],
}


class MedicationIdentifierTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Medication", "identifier", VIEW_DEFINITION)
