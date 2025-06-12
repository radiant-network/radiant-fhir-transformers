"""
FHIR RelatedPerson Communication transformer
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
            "related_person_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "communication",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "communication_language_coding": {
                "fhir_key": "language.coding",
                "type": "str",
            },
            "communication_language_text": {
                "fhir_key": "language.text",
                "type": "str",
            },
            "communication_preferred": {
                "fhir_key": "preferred",
                "type": "bool",
            },
        },
    },
]


class RelatedPersonCommunicationTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'RelatedPerson' resource in FHIR, focusing on the 'communication' element.

    This class transforms FHIR RelatedPerson JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'communication' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('RelatedPerson').
        subtype (str): Specifies the sub-element of the resource to focus on ('communication').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the RelatedPersonCommunicationTransformer instance with the resource type 'RelatedPerson',
            subtype 'communication', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("RelatedPerson", "communication", TRANSFORM_SCHEMA)
