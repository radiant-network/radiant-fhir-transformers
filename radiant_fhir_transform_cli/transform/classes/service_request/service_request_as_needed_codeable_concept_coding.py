"""FHIR ServiceRequest as_needed_codeable_concept_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "ServiceRequest",
    "name": "service_request_as_needed_codeable_concept_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
                {
                    "name": "service_request_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "asNeededCodeableConcept.coding",
            "column": [
                {
                    "name": "as_needed_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "as_needed_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "as_needed_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ServiceRequestAsNeededCodeableConceptCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("ServiceRequest", "as_needed_codeable_concept_coding", VIEW_DEFINITION)
