"""
FHIR Specimen Collection Fasting Status Codeable Concept Coding transformer
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
        "fhir_path": "collection.fastingStatusCodeableConcept.coding",
        "columns": {
            "collection_fasting_status_codeable_concept_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "collection_fasting_status_codeable_concept_coding_code": {
                "fhir_key": "code",
                "type": "str",
            },
            "collection_fasting_status_codeable_concept_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class SpecimenCollectionFastingStatusCodeableConceptCodingTransformer(
    FhirResourceTransformer
):
    """
    Transformer class for the 'Specimen' resource in FHIR, focusing on the 'collection.fastingStatusCodeableConcept.coding' element.

    This class transforms FHIR Specimen JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'collection.fastingStatusCodeableConcept.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Specimen').
        subtype (str): Specifies the sub-element of the resource to focus on ('collection.fastingStatusCodeableConcept.coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the SpecimenfastingStatusCodeableConceptCodingTransformer instance with the resource type 'Specimen',
            subtype 'collection.fastingStatusCodeableConcept.coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__(
            "Specimen",
            "collection_fasting_status_codeable_concept_coding",
            TRANSFORM_SCHEMA,
        )
