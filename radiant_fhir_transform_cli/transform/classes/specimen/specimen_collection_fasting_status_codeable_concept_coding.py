"""FHIR Specimen collection_fasting_status_codeable_concept_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_collection_fasting_status_codeable_concept_coding",
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
                    "name": "specimen_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "collection.fastingStatusCodeableConcept.coding",
            "column": [
                {
                    "name": "collection_fasting_status_codeable_concept_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_codeable_concept_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "collection_fasting_status_codeable_concept_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenCollectionFastingStatusCodeableConceptCodingTransformer(FhirResourceTransformer):
    resource_type = "Specimen"
    resource_component = "collection_fasting_status_codeable_concept_coding"
    view_definition = VIEW_DEFINITION
