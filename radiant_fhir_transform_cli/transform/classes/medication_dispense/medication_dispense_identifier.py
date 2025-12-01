"""FHIR MedicationDispense identifier transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "MedicationDispense",
    "name": "medication_dispense_identifier",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "medication_dispense_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "identifier",
            "column": [
                {"name": "identifier_use", "path": "use", "type": "string"},
                {"name": "identifier_system", "path": "system", "type": "string"},
                {"name": "identifier_value", "path": "value", "type": "string"},
            ],
        },
    ],
}


class MedicationDispenseIdentifierTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("MedicationDispense", "identifier", VIEW_DEFINITION)
