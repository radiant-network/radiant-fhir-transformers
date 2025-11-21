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


class SpecimenCollectionFastingStatusCodeableConceptCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "Specimen",
            "collection_fasting_status_codeable_concept_coding",
            VIEW_DEFINITION,
        )
