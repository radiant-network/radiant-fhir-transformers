"""FHIR Specimen container transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Specimen",
    "name": "specimen_container",
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
            "forEachOrNull": "container",
            "column": [
                {
                    "name": "container_identifier",
                    "path": "identifier",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "container_description",
                    "path": "description",
                    "type": "string",
                },
                {
                    "name": "container_type_coding",
                    "path": "type.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "container_type_text",
                    "path": "type.text",
                    "type": "string",
                },
                {
                    "name": "container_capacity_value",
                    "path": "capacity.value",
                    "type": "string",
                },
                {
                    "name": "container_capacity_unit",
                    "path": "capacity.unit",
                    "type": "string",
                },
                {
                    "name": "container_capacity_system",
                    "path": "capacity.system",
                    "type": "string",
                },
                {
                    "name": "container_capacity_code",
                    "path": "capacity.code",
                    "type": "string",
                },
                {
                    "name": "container_specimen_quantity_value",
                    "path": "specimenQuantity.value",
                    "type": "string",
                },
                {
                    "name": "container_specimen_quantity_unit",
                    "path": "specimenQuantity.unit",
                    "type": "string",
                },
                {
                    "name": "container_specimen_quantity_system",
                    "path": "specimenQuantity.system",
                    "type": "string",
                },
                {
                    "name": "container_specimen_quantity_code",
                    "path": "specimenQuantity.code",
                    "type": "string",
                },
                {
                    "name": "container_additive_codeable_concept_coding",
                    "path": "additiveCodeableConcept.coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "container_additive_codeable_concept_text",
                    "path": "additiveCodeableConcept.text",
                    "type": "string",
                },
                {
                    "name": "container_additive_reference_reference",
                    "path": "additiveReference.reference",
                    "type": "string",
                },
                {
                    "name": "container_additive_reference_display",
                    "path": "additiveReference.display",
                    "type": "string",
                },
                {
                    "name": "container_additive_reference_type",
                    "path": "additiveReference.type",
                    "type": "string",
                },
            ],
        },
    ],
}


class SpecimenContainerTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Specimen", "container", VIEW_DEFINITION)
