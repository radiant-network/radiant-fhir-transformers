"""
FHIR Specimen Container transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "specimen_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "container",
        "columns": {
            "container_identifier": {"fhir_key": "identifier", "type": "str"},
            "container_description": {"fhir_key": "description", "type": "str"},
            "container_type_text": {"fhir_key": "type.text", "type": "str"},
            "container_type_coding": {"fhir_key": "type.coding", "type": "str"},
            "container_capacity_value": {
                "fhir_key": "capacity.value",
                "type": "str",
            },
            "container_capacity_unit": {
                "fhir_key": "capacity.unit",
                "type": "str",
            },
            "container_capacity_system": {
                "fhir_key": "capacity.system",
                "type": "str",
            },
            "container_capacity_code": {
                "fhir_key": "capacity.code",
                "type": "str",
            },
            "specimen_quantity_value": {
                "fhir_key": "specimenQuantity.value",
                "type": "str",
            },
            "specimen_quantity_unit": {
                "fhir_key": "specimenQuantity.unit",
                "type": "str",
            },
            "specimen_quantity_system": {
                "fhir_key": "specimenQuantity.system",
                "type": "str",
            },
            "specimen_quantity_code": {
                "fhir_key": "specimenQuantity.code",
                "type": "str",
            },
            "specimen_additive_codeable_concept_text": {
                "fhir_key": "specimen.additiveCodeableConcept.text",
                "type": "str",
            },
            "specimen_additive_codeable_concept_coding": {
                "fhir_key": "specimen.additiveCodeableConcept.coding",
                "type": "str",
            },
            "specimen_additive_reference_reference": {
                "fhir_key": "specimen.additiveReference.reference",
                "type": "str",
            },
            "specimen_additive_reference_display": {
                "fhir_key": "specimen.additiveReference.display",
                "type": "str",
            },
        },
    },
]


class SpecimenContainerTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'container' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'container' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('container').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenContainer instance with the resource type 'Specimen',
            subtype 'container', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Specimen", "container", TRANSFORM_SCHEMA)
